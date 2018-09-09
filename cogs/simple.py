from discord.ext import commands
import asyncio
import discord
import random

# Simple toy commands.
class Simple:

  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context=True)
  async def choke(self, ctx, target):
    return await self.bot.say("choke me " + target + " daddy")

  @commands.command(pass_context=True)
  async def troutslap(self, ctx, target):
    return await self.bot.say("*slaps " + target + " with a trout*")

  @commands.command(pass_context=True)
  async def eight_ball(self, ctx):
    eight_ball_sayings = [
      "It is certain",
      "It is decidedly so",
      "Without a doubt",
      "Yes, definitely",
      "You may rely on it",
      "As I see it, yes",
      "Most likely",
      "Outlook good",
      "Yes",
      "Signs point to yes",
      "Reply hazy, try again",
      "Ask again later",
      "Better not tell you now",
      "Cannot predict now",
      "Concentrate and ask again",
      "Don\'t count on it",
      "My reply is no",
      "My sources say no",
      "Outlook not so good",
      "Very doubtful" 
    ]

    # TODO: @ the user
    return await self.bot.say(random.choice(eight_ball_sayings))

  @commands.command(pass_context=True)
  async def coin(self, ctx):
    n = random.randint(0, 1)
    flip = "tails" if n == 0 else "heads"
    return await self.bot.say("You flipped " + flip + "!")

  @commands.command(pass_context=True)
  async def roll(self, ctx, n):
    if 'd' in n:
      dice = n.split('d')
      string = ''
      total = 0
      for i in range(int(dice[0])):
        roll = random.randint(1, int(dice[1]))
        total += roll
        if i < int(dice[0]) - 1:
          string += str(roll) + ' + '
        else:
          string += str(roll)
      await self.bot.say(string)
      return await self.bot.say('Total: ' + str(total))
    else:
      return await self.bot.say(random.randint(1, int(n)))

  @commands.command(pass_context=True)
  async def roll_eldritch(self, ctx, n):
    successes = 0
    result = ""
    n = int(n)
    if n > 1000:
        return await ctx.send("Cthulhu wins.")
    for i in range(0, n):
        roll = random.randint(1, 6)
        result += str(roll) + " "
        if roll >= 5:
            successes += 1
    await self.bot.say(result)
    return await self.bot.say(str(successes) + " successes!")

  @commands.command(pass_context=True)
  async def send(self, ctx, chan_name, msg):
    channels = { 
      "#anime" : 237776682100981760,
      "#bored_games" : 333128096733724672,
      "#electrogames" : 237776811021303808,
      "#movies" : 237776499267207169,
      "#music" : 237776707052896257,
      "#sports" : 238837234172690432,
      "#television" : 237776634822918144,
      "#off-topic" : 237775894578462720,
      "#politics" : 251567712654852096,
      "#alexhateboard" : 316399024473374722
    }
    channel = self.bot.get_channel(str(channels[chan_name]))
    if "!topic-" in message.content:
      topic = message.content.split(' ')[1][7:]
    return await self.bot.send_message(channel, ctx.message.author.name + \
      " says about " + topic + ":\n" + msg)

def setup(bot):
    bot.add_cog(Simple(bot))