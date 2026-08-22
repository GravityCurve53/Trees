import discord
from discord.ext import commands
import asyncio
import random

token = input("pick discord token: ")

intents = discord.Intents.default()

ABSOLUTE_CINEMA = [
    "im a tree",
    "did you know that im a tree?",
    "the sun is so tasty :]",
    "fun tree facts #2763: trees have leaves",
    "minecraft spruce trees are innacurate to real life spruce trees, I take this as offensive",
    "me when I tree:",
    "fr",
    "fun tree facts #2809: trees are basically immortal",
    "remember to use the right your when writing your discord messages",
    ":3",
    ":3", # twice the chances of landing on this
    "tree",
    "In botany, a tree is a perennial plant with an elongated stem, or trunk, usually supporting branches and leaves. In some usages, the definition of a tree may be narrower, e.g., including only woody plants with secondary growth, only plants that are usable as lumber, or only plants above a specified height. Wider definitions include taller palms, tree ferns, bananas, and bamboos.",
    "who just copy pasted the opening paragraph of the wikipedia page for trees :sob:",
    ":deciduous_tree:",
    "@everyone STOP GLOBAL WARMING",
    "fun tree facts #2998: trees are made out of wood",
    "remember to stay calm"
]

ForestChannels = [
    # put your own channels here bro
]

bot = commands.Bot(command_prefix="/", intents=intents)

async def send_message(Content, ID):
    channel = await bot.fetch_channel(ID)
    await channel.send(Content)

@bot.event
async def on_ready():
    print("ITS FREE ROBUX TIME")
    await DoTreeThings()

async def DoTreeThings():
    while True:
        await send_message(random.choice(ABSOLUTE_CINEMA), random.choice(ForestChannels))
        await asyncio.sleep(random.randint(7, 10))
bot.run(token)
