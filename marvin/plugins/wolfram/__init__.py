import asyncio
from ..base import BaseHandler
import wolframalpha
from .config import WOLFRAM_API_KEY


class WolframHandler(BaseHandler):
    def __init__(self, bot):
        super().__init__(bot)

        self._wolfram = wolframalpha.Client(WOLFRAM_API_KEY)

    @asyncio.coroutine
    def on_message(self, message):
        text = message.get('text', '').lower()
        channel = message['channel']

        if text.endswith('는?') or text.endswith('은?'):
            query = text[:-2]
            response = self._wolfram.query(query)
            pod = next(response.results)
            if not pod:
                yield from self.send_text(channel, '뭘 원하시는 건지 모르겠어요')
            else:
                yield from self.send_text(channel, pod.text)
