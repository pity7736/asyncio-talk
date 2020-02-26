from flask import Flask

sync_app = Flask('sync-app')


@sync_app.route('/')
def index():
    return {'hello': 'world'}
