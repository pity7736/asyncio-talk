import asyncio


async def coro(delay):
    print(f'coro sleeping {delay} seconds!')
    sleep = asyncio.sleep(delay)
    print('sleep', sleep)
    await sleep
    print('coro finish!')


if __name__ == '__main__':
    import sys
    c = coro(int(sys.argv[1]))
    print(c, type(c))
    asyncio.run(c)
