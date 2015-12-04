import asyncio
from .base import BaseHandler


number_emojis = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


class VoteHandler(BaseHandler):
    @asyncio.coroutine
    def on_message(self, message):
        text = message.get('text', '').lower()
        channel = message['channel']
        timestamp = message['ts']

        if text.startswith('투표'):
            args = text.split()[1:]
            if not args or args[0] == '찬반':
                self.api.reactions.add('o', channel=channel, timestamp=timestamp)
                self.api.reactions.add('x', channel=channel, timestamp=timestamp)
            elif args[0].isdigit():
                n = int(args[0])
                if n > 9:
                    yield from self.send_text(channel, '너무 많아요')
                    return

                for i in range(n):
                    emoji = number_emojis[i]
                    self.api.reactions.add(emoji, channel=channel, timestamp=timestamp)

