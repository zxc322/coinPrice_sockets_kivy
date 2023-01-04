import asyncio
import json
import websockets

from my_redis import RedisPool


class CoinData:

    def __init__(self, url: str, pairs: list):
        self.url = url
        self.pairs = pairs
        self.redis = RedisPool()
        self.tasks = list()

    async def get_coin_data(self, pair: str):
        url = self.url.format(pair)
        print(f'Start socker || url: {url}')
        async with websockets.connect(url) as client:
            while True:
                data = json.loads(await client.recv())['data']
                price = float(data['c'])
                self.redis.set_price(key=pair, value=price)

    async def run_sockets(self):
        for pair in self.pairs:
            task = asyncio.create_task(self.get_coin_data(pair=pair))
            self.tasks.append(task)
        await asyncio.gather(*self.tasks)

