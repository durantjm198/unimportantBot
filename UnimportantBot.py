import discord
from discord.ext.commands import Bot
import asyncio
import os

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
        print(f'Failed to load extension {extension}.', file=sys.stderr)
        traceback.print_exc()

############################## TWITTER IMAGES #################################
@bot.event
async def on_message(message):
  is_tweet = message.content.startswith('https://twitter.com') or \
             message.content.startswith('https://www.twitter.com')
  if is_tweet:
    return await bot.send_message(message.channel, 'That looks like a tweet!')

bot.run(token)