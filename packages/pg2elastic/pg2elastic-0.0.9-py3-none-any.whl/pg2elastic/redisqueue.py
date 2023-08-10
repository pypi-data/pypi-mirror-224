"""PGSync RedisQueue."""
import json
from typing import List, Optional

from redis import Redis
from redis.backoff import ExponentialBackoff
from redis.retry import Retry
from .settings import REDIS_READ_CHUNK_SIZE, REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD, \
    REDIS_USERNAME, REDIS_SOCKET_TIMEOUT, REDIS_ENDPOINT
from loguru import logger
from redis.exceptions import (
    BusyLoadingError,
    ConnectionError,
    TimeoutError
)


class RedisQueue(object):
    """Simple Queue with Redis Backend."""

    def __init__(self, name: str, namespace: str = "queue", **kwargs):
        """Init Simple Queue with Redis Backend."""
        self.key: str = f"{namespace}:{name}"

        host = kwargs.get('host', '') or REDIS_ENDPOINT or REDIS_HOST
        username = kwargs.get('REDIS_USERNAME', '') or REDIS_USERNAME
        password = kwargs.get('REDIS_PASSWORD', '') or REDIS_PASSWORD
        port = kwargs.get('port', 6379) or REDIS_PORT
        db = kwargs.get('db', 0) or REDIS_DB

        authentication_params = {'host': host, 'db': db, 'port': port}

        if username:
            authentication_params.update({'username': username})

        if password:
            authentication_params.update({'password': password})

        try:
            retry = Retry(ExponentialBackoff(), 3)
            self.__db: Redis = Redis(
                **authentication_params,
                socket_timeout=REDIS_SOCKET_TIMEOUT,
                retry=retry,
                retry_on_error=[BusyLoadingError, ConnectionError, TimeoutError]
            )
            self.__db.ping()
        except ConnectionError as e:
            logger.exception(f"Redis server is not running: {e}")
            raise

    @property
    def qsize(self) -> int:
        """Return the approximate size of the queue."""
        return self.__db.llen(self.key)

    def pop(self, chunk_size: Optional[int] = None) -> List[dict]:
        """Remove and return multiple items from the queue."""
        chunk_size = chunk_size or REDIS_READ_CHUNK_SIZE
        if self.qsize > 0:
            pipeline = self.__db.pipeline()
            pipeline.lrange(self.key, 0, chunk_size - 1)
            pipeline.ltrim(self.key, chunk_size, -1)
            items: List = pipeline.execute()
            logger.debug(f"pop size: {len(items[0])}")
            return list(map(lambda value: json.loads(value), items[0]))

    def push(self, items: List) -> None:
        """Push multiple items onto the queue."""
        self.__db.rpush(self.key, *map(json.dumps, items))

    def delete(self) -> None:
        """Delete all items from the named queue."""
        logger.info(f"Deleting redis key: {self.key}")
        self.__db.delete(self.key)
