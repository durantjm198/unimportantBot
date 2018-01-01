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
    for extension in extensions:
      try:
        self.load_extension(extension)
      except Exception as e:
        print('Failed to load extension.', file=sys.stderr)
        traceback.print_exc()
    super().run(config.token)

    async def on_message(self, message):
      if message.author.bot:
        return
      await self.process_commands(message)

bot = UnimportantBot()