from asyncio_talk.sync_api import sync_app


if __name__ == '__main__':
    sync_app.run(host='0.0.0.0', port=8000, debug=True)
