import discord
from discord.ext.commands import Bot
from cogs.utils import context
import asyncio
import sys
import traceback
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
    super().run(config.token)

    async def process_commands(self, message):
      ctx = await self.get_context(message)

      if ctx.command is None:
        return

      async with ctx.acquire():
        await self.invoke(ctx)

    async def on_message(self, message):
      if message.author.bot:
        return
      await self.process_commands(message)

bot = UnimportantBot()