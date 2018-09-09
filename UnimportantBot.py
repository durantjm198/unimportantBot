import asyncio
import config
import discord
from discord.ext import commands
import sys
import traceback

extensions = (
  'cogs.simple',
  'cogs.twitter',
)

class UnimportantBot(commands.Bot):
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
      server = message.server
      if message.author.bot || '!nobot' in message.content:
        return
      await self.process_commands(message)

bot = UnimportantBot()