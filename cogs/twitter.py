from discord.ext import commands
import asyncio
import discord
import tweepy

# Twitter.
class Twitter:
  def __init__(self, bot):
    self.bot = bot

  async def on_message(self, message):
    is_tweet = message.content.startswith('https://twitter.com') or \
             message.content.startswith('https://www.twitter.com')
    if is_tweet:
      return await self.bot.send_message(message.channel, 'That looks like a tweet!')

def setup(bot):
    bot.add_cog(Twitter(bot))