import json
import asyncio
from .base import BaseHandler


class HitchhikerHandler(BaseHandler):
    @asyncio.coroutine
    def on_message(self, message):
        text = message.get('text', '').lower()
        channel = message['channel']

        if 'life' in text or '삶' in text:
            yield from self.send_text(channel, '''Life! don't talk to me about life.''')

        elif 'idea' in text or '아이디어' in text:
            yield from self.send_text(channel, '''I have a million ideas. They all point to certain death.''')

        elif '계산' in text:
            yield from self.send_text(channel, '''I could calculate your chance of survival, but you won’t like it.''')
