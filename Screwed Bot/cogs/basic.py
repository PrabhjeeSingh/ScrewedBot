import discord 
from discord.ext import commands,tasks
from discord.ext.commands import bot


class commandsEvent(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener
    async def on_ready(self):
            await discord.utils.get(guild.text_channels,name="general").channel.send("Hello")




def setup(bot):
    bot.add_Cog(commandsEvent(bot))
