import discord
from discord.ext import commands


client = commands.Bot(";")

@client.event
async def on_ready():
    await print("Yo i am online!")


client.load_extension("cogs.basic")


client.run("ODQxNjAzNzE4NDIyOTg2NzUy.YJpKig.rvigbO0mRrQW-utOPfrMhVGAL_8")