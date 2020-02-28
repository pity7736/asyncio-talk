import asyncio
import time

from flask import Flask

from asyncio_talk.common import sync_request, async_request


sync_app = Flask('sync-app')


@sync_app.route('/')
def index():
    return {'hello': 'world'}


@sync_app.route('/request')
def request():
    r = sync_request('https://www.google.com')
    time.sleep(10)
    return {'ok': r.ok}


@sync_app.route('/async-request')
def arequest():
    print('"async" request')
    loop = asyncio.new_event_loop()
    # add sleep
    loop.run_until_complete(async_request('https://www.google.com', loop))
    loop.close()
    return {'ok': True}
