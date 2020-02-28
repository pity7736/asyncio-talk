import time

import httpx
import requests


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