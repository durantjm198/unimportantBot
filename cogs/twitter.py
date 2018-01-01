from discord.ext import commands
import asyncio
import discord
import tweepy
import config

# Twitter.
class Twitter:
  def __init__(self, bot):
    self.bot = bot
    auth = tweepy.OAuthHandler(bot.tw_consumer_key, bot.tw_consumer_secret)
    auth.set_access_token(bot.tw_access_token, bot.tw_access_token_secret)
    self.api = tweepy.API(auth)

  async def on_message(self, message):
    is_tweet = message.content.startswith('https://twitter.com') or \
             message.content.startswith('https://www.twitter.com')
    if is_tweet:
      return await self.bot.send_message(self.get_image_links(message))

  def get_image_links(self, message):
    return self.api.get_status(938188434195341313).text

def setup(bot):
    bot.add_cog(Twitter(bot))