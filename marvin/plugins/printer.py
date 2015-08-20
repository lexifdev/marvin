import asyncio
from .base import BaseHandler


class PrinterHandler(BaseHandler):
    @asyncio.coroutine
    def on_message(self, message):
        print(message)
