import discord
from discord.ext.commands import Bot
import asyncio
import sys
import config

extensions = (
  'cogs.simple',
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
    super().run(token)

bot = UnimportantBot()