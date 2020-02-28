import asyncio
import time

import requests
import uvloop

import httpx


sites = [
        'https://www.yahoo.com/',
        'http://www.cnn.com',
        'http://www.python.org',
        'http://www.jython.org',
        'http://www.pypy.org',
        'http://www.perl.org',
        'http://www.cisco.com',
        'http://www.facebook.com',
        'http://www.twitter.com',
        'http://www.macrumors.com/',
        'http://arstechnica.com/',
        'http://www.reuters.com/',
        'http://abcnews.go.com/',
        'http://www.cnbc.com/',
        'https://www.google.com/'
    ]


async def async_request(url, loop):
    init = loop.time()
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    print(f'site: {url}. response: {response}. time elapsed: {loop.time() - init}')


async def async_request2(client, url, loop):
    init = loop.time()
    response = await client.get(url)
    print(f'site: {url}. response: {response}. time elapsed: {loop.time() - init}')


def sync_request(url):
    init = time.monotonic()
    response = requests.get(url)
    print(f'site: {url}. response: {response}. time elapsed: {time.monotonic() - init}')


async def async_main():
    loop = asyncio.get_event_loop()
    # loop = uvloop.new_event_loop()
    # asyncio.set_event_loop(loop)
    tasks = (asyncio.create_task(async_request(url, loop)) for url in sites)
    init = loop.time()
    await asyncio.gather(*tasks)
    print(f'total time elapsed: {loop.time() - init}')


async def async_main2():
    # loop = asyncio.get_event_loop()
    loop = uvloop.new_event_loop()
    init = loop.time()
    asyncio.set_event_loop(loop)
    client = httpx.AsyncClient()
    tasks = (asyncio.create_task(async_request2(client, url, loop)) for url in sites)
    await asyncio.gather(*tasks)
    await client.aclose()
    print(f'total time elapsed: {loop.time() - init}')


def sync_main():
    init = time.monotonic()
    for url in sites:
        sync_request(url)
    print(f'total time elapsed: {time.monotonic() - init}')


if __name__ == '__main__':
    import sys
    arg = sys.argv[1]
    if arg == 'sync':
        sync_main()
    elif arg == 'async2':
        asyncio.run(async_main2())
    else:
        asyncio.run(async_main())
