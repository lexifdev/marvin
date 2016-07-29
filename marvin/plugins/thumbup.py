import asyncio
import random
from .base import BaseHandler


class AgreeHandler(BaseHandler):
    @asyncio.coroutine
    def on_message(self, message):
        text = message.get('text', '').lower()
        channel = message['channel']

        if text in [':+1:', ':thumbsup:']:
            yield from self.send_text(channel, ':+1:')
