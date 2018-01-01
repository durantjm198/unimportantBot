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
    return await bot.say("choke me " + target + " daddy")

  @commands.command(pass_context=True)
  async def troutslap(self, ctx, target):
    return await bot.say("*slaps " + target + " with a trout*")

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
    return await bot.say(rng.choice(eight_ball_sayings))

  @commands.command(pass_context=True)
  async def coin(self, ctx):
    n = random.randint(0, 1)
    flip = "tails" if n == 0 else "heads"
    return await bot.say("You flipped " + flip + "!")

  # TODO: roll 2d20
  @commands.command(pass_context=True)
  async def roll(self, ctx, n):
    return await bot.say(random.randint(1, int(n)))

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
    await bot.say(result)
    return await bot.say(str(successes) + " successes!")

def setup(bot):
    bot.add_cog(Simple(bot))