import asyncio


async def coro(delay):
    print(f'coro sleeping {delay} seconds!')
    await asyncio.sleep(delay)
    print('coro finish!')


if __name__ == '__main__':
    import sys
    asyncio.run(coro(int(sys.argv[1])))
