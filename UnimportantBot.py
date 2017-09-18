import discord
from discord.ext.commands import Bot
import asyncio
import random
import os

bot = Bot(command_prefix="!")
token = os.environ['api_key']
sc_entries = []
votes = []

############################### SONG CONTEST ###################################
class SongContestEntry:
    def __init__(self, entry_name, song_title, artist, link, submitter):
        self.entry_name = entry_name
        self.song_title = song_title
        self.artist = artist
        self.link = link
        self.submitted_by = submitter
        self.points = 0
        self.voters = []

    def __str__(self):
        return self.entry_name + ": " + self.artist + " -- " + self.song_title \
               + " -- " + self.link + " -- " + str(self.points) + " points"

class Vote:
    def __init__(self, voter, entry_name, points):
        self.voter = voter
        self.entry_name = entry_name
        self.points = points

@bot.command(pass_context = True)
async def add_entry(ctx, entry_name, song_title, artist, link):
    this_entry = SongContestEntry(entry_name, song_title,                 \
                                  artist, link, ctx.message.author)
    for entry in sc_entries:
        if entry.entry_name == this_entry.entry_name:
            return await bot.say("Entry name already taken!")
        if entry.submitted_by == ctx.message.author:
            return await bot.say("You already entered "+entry.entry_name + "!")
    sc_entries.append(this_entry)
    return await bot.say(entry_name + " added!")

@bot.command()
async def print_entries():
    for entry in sc_entries:
        await bot.say(entry)
    return

@bot.command(pass_context=True)
async def vote(ctx, entry_name, points):
    points = int(points)
    if points == None:
        return await bot.say("That's not a number!")

    voter = ctx.message.author
    vote = Vote(voter, entry_name, points)
    if points > 10 or points == 9 or points == 7 or points < 1:
        return await bot.say("Remember the voting system! You can only give 10, 8, 6, 5, 4, 3, 2, or 1 points!")
    for v in votes:
        if v.voter == voter and v.points == points:
            return await bot.say("You already voted for " + v.entry_name + " to receive " + str(points) + " points!")
    for entry in sc_entries:

        if entry.entry_name == entry_name:
            if entry.submitted_by == voter:
                return await bot.say("You can't vote for yourself!")
            
            for entry_voter in entry.voters:
                if entry_voter == voter:
                    return await bot.say("You already voted for this song!")

            entry.points += points
            entry.voters.append(voter)
            votes.append(vote)
            return await bot.say("Vote received!")
    
    return await bot.say("That's not an entry!")

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


bot.run(token)