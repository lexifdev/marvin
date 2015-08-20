import asyncio
from .base import BaseHandler


class PingPongHandler(BaseHandler):
    @asyncio.coroutine
    def on_message(self, message):
        if message.get('text', '').endswith('ping'):
            yield from self.send_text(message['channel'], 'pong')
