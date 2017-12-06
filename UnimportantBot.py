import discord
from discord.ext.commands import Bot
import asyncio
import random
import os

bot = Bot(command_prefix="!")
token = os.environ['api_key']
sc_entries = []
votes = []

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
  "Consentrate and ask again",
  "Don\'t count on it",
  "My reply is no",
  "My sources say no",
  "Outlook not so good",
  "Very doubtful" ]

############################## TWITTER IMAGES #################################
@bot.event
async def on_message(message):
  is_tweet = message.content.startswith('https://twitter.com') or \
             message.content.startswith('https://www.twitter.com')
  if is_tweet:
    return await bot.say('That looks like a tweet!')

################################ MISCELLANY ###################################

@bot.event
async def on_read():
    print("Client logged in")

@bot.command()
async def troutslap(target):
    return await bot.say("*slaps " + target + " with a trout*")

@bot.command()
async def roll(n):
    return await bot.say(random.randint(1, int(n)))

@bot.command()
async def roll_eldritch(n):
    successes = 0
    result = ""
    n = int(n)
    if n > 1000:
        return await bot.say("Cthulhu wins.")
    for i in range(0, n):
        roll = random.randint(1, 6)
        result += str(roll) + " "
        if roll >= 5:
            successes += 1
    await bot.say(result)
    return await bot.say(str(successes) + " successes!")

@bot.command()
async def coin():
    n = random.randint(0, 1)
    flip = "tails" if n == 0 else "heads"
    return await bot.say("You flipped " + flip + "!")

@bot.command()
async def choke(target):
    return await bot.say("choke me " + target + " daddy")

bot.run(token)
