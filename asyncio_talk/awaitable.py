import asyncio


class Awaitable:

    def __init__(self, delay):
        self._delay = delay

    def __await__(self):
        a = self._coro().__await__()
        print(a)
        return a

    async def _coro(self):
        print(f'awaitable coro, sleeping {self._delay} seconds!')
        await asyncio.sleep(self._delay)
        print('finish awaitable coro')


async def main():
    awaitable = Awaitable(5)
    print(awaitable)
    await awaitable


if __name__ == '__main__':
    asyncio.run(main())
