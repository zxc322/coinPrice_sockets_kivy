import redis


class RedisPool:

    def __init__(self, host: str = 'localhost', port: int = 6379):
        self.pool = self._init_redis_pool(host=host, port=port)

    @staticmethod
    def _init_redis_pool(host: str, port: int) -> redis.Redis:
        redis_c = redis.Redis(
            host=host,
            port=port
        )
        return redis_c

    def set_price(self, key: str, value: float) -> None:
        self.pool.set(key, value)

    def get_price(self, key: str) -> float:
        price = self.pool.get(key)
        return float(price) if price else 0.0
