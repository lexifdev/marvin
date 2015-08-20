import json
import asyncio


class PingPongHandler(object):
    @asyncio.coroutine
    def on_message(self, sock, message):
        if message.get('text', '').endswith('ping'):
            yield from sock.send(json.dumps({
                'type': 'message',
                'channel': message['channel'],
                'text': 'pong'
            }))
