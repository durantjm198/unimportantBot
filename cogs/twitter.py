from discord.ext import commands
import asyncio
import discord
import tweepy

# Twitter.
class Twitter:
  def __init__(self, bot):
    self.bot = bot
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    self.api = tweepy.API(auth)

  async def on_message(self, message):
    is_tweet = message.content.startswith('https://twitter.com') or \
             message.content.startswith('https://www.twitter.com')
    if is_tweet:
      return await self.bot.send_message(get_image_links(message))

  def get_image_links(message):
    return self.api.get_status(938188434195341313).text


def setup(bot):
    bot.add_cog(Twitter(bot))