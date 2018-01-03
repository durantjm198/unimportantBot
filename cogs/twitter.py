from discord.ext import commands
import asyncio
import discord
import tweepy
import re
import sys

# Twitter.
class Twitter:
  def __init__(self, bot):
    self.bot = bot
    auth = tweepy.OAuthHandler(bot.tw_consumer_key, bot.tw_consumer_secret)
    auth.set_access_token(bot.tw_access_token, bot.tw_access_token_secret)
    self.api = tweepy.API(auth)

  async def on_message(self, message):
    if 'twitter.com' in message.content:
      await self.bot.send_message(message.channel, self.process_tweet(message))

  def process_tweet(self, message):
    tweet = self.get_tweet(message)
    quote = self.get_quote(tweet)
    links = self.get_media_links(tweet)
    print(links)
    if quote or links:
      return quote + '\n' + ' '.join(links[1:])
     
  def get_tweet(self, message):
    url = re.search("twitter.com\/\w+\/status\/\d+", message.content).group()
    return self.api.get_status(url.split('/')[-1], tweet_mode='extended')

  def get_media_links(self, tweet):
    try:
      links = [med['media_url'] for med in tweet.extended_entities['media']]
      return [link for link in links] if len(links) > 1 else ''
    except:
      print("Exception caught! ", sys.exc_info()[0])
      return ''

  def get_quote(self, tweet):
    quote = "Quoted tweet: https://twitter.com/statuses/"
    if tweet.is_quote_status:
      return quote + tweet.quoted_status['id_str']
    else:
      return ''

def setup(bot):
    bot.add_cog(Twitter(bot))