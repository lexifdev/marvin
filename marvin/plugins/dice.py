import asyncio
import random
from .base import BaseHandler


class DiceHandler(BaseHandler):
    @asyncio.coroutine
    def on_message(self, message):
        text = message.get('text', '').lower()
        channel = message['channel']

        if text.startswith('dice'):
            args = text.split(' ', 3)
            args_length = len(args)

            try:
                if args_length == 2:
                    arg = int(args[1])
                    result = random.randint(1, arg)
                    yield from self.send_text(channel, str(result))
                elif args_length == 3:
                    arg1 = int(args[1])
                    arg2 = int(args[2])
                    result = random.randint(arg1, arg2)
                    yield from self.send_text(channel, str(result))
                else:
                    raise ValueError
            except ValueError:
                yield from self.send_text(channel, 'pardon?')
