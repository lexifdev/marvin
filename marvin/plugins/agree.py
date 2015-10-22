import asyncio
import random
from .base import BaseHandler


class AgreeHandler(BaseHandler):
    @classmethod
    def weighted_random(cls, ms):
        p = []
        for weight, value in ms:
            p += weight * [value]

        return random.choice(p)

    @asyncio.coroutine
    def on_message(self, message):
        text = message.get('text', '').lower()
        channel = message['channel']

        if text.endswith('그렇지?') or text.endswith('그러니?'):
            result = self.weighted_random([
                (2, '그럼요'),
                (2, '물론이죠'),
                (1, '아닐걸요'),
                (1, '그럴리가요'),
                (1, '전 모르겠어요'),
            ])

            yield from self.send_text(channel, result)
