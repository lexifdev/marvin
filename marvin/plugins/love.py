import asyncio
from .base import BaseHandler


class LoveHandler(BaseHandler):
    @asyncio.coroutine
    def on_message(self, message):
        if message.get('text', '').endswith('사랑해'):
            yield from self.send_text(message['channel'], '저두요')
