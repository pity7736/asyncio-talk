import asyncio


async def coro(delay):
    print(f'coro sleeping {delay} seconds!')
    sleep = asyncio.sleep(delay)
    print('sleep', sleep)
    await sleep
    print('coro finish!')


async def main():
    task = asyncio.create_task(coro(5))
    await task
    print('sleep main')
    await asyncio.sleep(3)
    print('finish!')


asyncio.run(main())
