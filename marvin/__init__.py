import json
import requests
import websockets
import asyncio
from marvin import plugins


class PrintHandler(object):
    @asyncio.coroutine
    def on_message(self, sock, message):
        print(message)


class Marvin(object):
    def __init__(self, token):
        self._token = token
        self._handlers = [
            PrintHandler(),
            plugins.PingPongHandler(),
        ]

    @asyncio.coroutine
    def _loop(self, slack_info):
        sock = yield from websockets.connect(slack_info['url'])
        while True:
            message = yield from sock.recv()
            for handler in self._handlers:
                yield from handler.on_message(sock, json.loads(message))

    def start(self):
        response = requests.get('https://slack.com/api/rtm.start', {
            'token': self._token
        })
        slack_info = response.json()

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._loop(slack_info))
