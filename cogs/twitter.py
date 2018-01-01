from discord.ext import commands
import asyncio
import discord
############################## TWITTER IMAGES #################################
@bot.event
async def on_message(message):
  is_tweet = message.content.startswith('https://twitter.com') or \
             message.content.startswith('https://www.twitter.com')
  if is_tweet:
    return await bot.send_message(message.channel, 'That looks like a tweet!')