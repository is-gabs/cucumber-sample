from typing import Optional

from redis import Redis, RedisError

from src import settings


class Client:
    def __init__(self):
        self._client = Redis(
            host=settings.CACHE_HOST,
            port=settings.CACHE_PORT
        )

    def get(self, name: str, default: Optional[str] = None) -> Optional[str]:
        try:
            result = self._client.get(name=name)
            if result:
                result = result.decode()
            else:
                result = default
        except RedisError:
            result = default

        return result
