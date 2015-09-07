import asyncio
import random
from .base import BaseHandler


class AgreeHandler(BaseHandler):
    @asyncio.coroutine
    def on_message(self, message):
        text = message.get('text', '').lower()
        channel = message['channel']

        n_k = text.count('ㅋ')
        if n_k > 1:
            yield from self.send_text(channel, 'ㅋ' * (n_k + 2))
