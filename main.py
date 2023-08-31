import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the youtube bot")

client.run('MTE0NjY2MjgwNDAxNTgyODk5Mg.GgWSsL.cREkQrhWKu_2tH31PIqZkiwgNLZr2AWz1_CuIU')