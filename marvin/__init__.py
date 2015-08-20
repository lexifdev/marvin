import json
from urllib.parse import urlparse
import requests
import websockets
import websockets.client
import asyncio
from marvin import plugins


class Marvin(object):
    def __init__(self, token):
        self._token = token
        self._sock = None
        self._handlers = [
            plugins.PrinterHandler(self),
            plugins.PingPongHandler(self),
            plugins.HitchhikerHandler(self),
        ]

    @asyncio.coroutine
    def send_text(self, channel, text):
        yield from self._sock.send(json.dumps({
            'type': 'message',
            'channel': channel,
            'text': text,
        }))

    @asyncio.coroutine
    def _main_loop(self, url):
        self._sock = yield from websockets.connect(url)
        while True:
            raw_message = yield from self._sock.recv()
            for handler in self._handlers:
                message = json.loads(raw_message)
                if 'type' in message and message['type'] == 'message':
                    yield from handler.on_message(message)

    def start(self):
        response = requests.get('https://slack.com/api/rtm.start', {
            'token': self._token
        })
        slack_info = response.json()
        url = slack_info['url']

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._main_loop(url))
