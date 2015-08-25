import asyncio
import random
from .base import BaseHandler


class AgreeHandler(BaseHandler):
    @asyncio.coroutine
    def on_message(self, message):
        text = message.get('text', '').lower()
        channel = message['channel']

        if text.endswith('그렇지?') or text.endswith('그러니?'):
            result = random.choice(['그럼요', '물론이죠', '아닐걸요', '그럴리가요', '전 모르겠어요'])
            yield from self.send_text(channel, result)
