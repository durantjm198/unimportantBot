import discord
from discord.ext.commands import Bot
import asyncio
import sys
import traceback
import config

extensions = (
  'cogs.simple',
  'cogs.twitter',
)

class UnimportantBot(Bot):
  def __init__(self):
    super().__init__(command_prefix = '!')
    self.token = config.token
    self.tw_consumer_key = config.tw_consumer_key
    self.tw_consumer_secret = config.tw_consumer_secret
    self.tw_access_token = config.tw_access_token
    self.tw_access_token_secret = config.tw_access_token_secret

    for extension in extensions:
      try:
        self.load_extension(extension)
      except Exception as e:
        print('Failed to load extension.', file=sys.stderr)
        traceback.print_exc()
    super().run(self.token)

    async def on_message(self, message):
      if message.author.bot:
        return
      await self.process_commands(message)

bot = UnimportantBot()