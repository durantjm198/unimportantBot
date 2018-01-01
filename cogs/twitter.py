from discord.ext import commands
import asyncio
import discord
import tweepy
import re

# Twitter.
class Twitter:
  def __init__(self, bot):
    self.bot = bot
    auth = tweepy.OAuthHandler(bot.tw_consumer_key, bot.tw_consumer_secret)
    auth.set_access_token(bot.tw_access_token, bot.tw_access_token_secret)
    self.api = tweepy.API(auth)

  async def on_message(self, message):
    if 'twitter.com' in message.content:
      for link in self.get_image_links(message):
        await self.bot.send_message(message.channel, link)

  def get_tweet(self, message)
    url = re.search("twitter.com\/\w+\/status\/\d+", message.content).group()
    tweet = self.api.get_status(url.split('/')[-1])

  def get_image_links(self, message):
    tweet = self.get_tweet(message)
    return [med.media_url for med in tweet.extended_entities.media]

def setup(bot):
    bot.add_cog(Twitter(bot))