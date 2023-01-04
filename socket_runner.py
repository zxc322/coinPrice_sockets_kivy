import sys
import asyncio

from binance_sockets import CoinData
from config import URL, PAIRS


if __name__ == '__main__':
    try:
        runner = CoinData(url=URL, pairs=PAIRS)
        asyncio.run(runner.run_sockets())
    except KeyboardInterrupt:
        sys.exit(0)
