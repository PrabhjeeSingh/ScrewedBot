import discord,random,os
from discord import message
from discord.ext import commands,tasks
from itertools import cycle
import json
# from discord.ext.commands import Bot


def get_prefix(client,message):
    with open('prefix.json','r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

# client = discord.Client()
#client = commands.Bot(command_prefix=get_prefix)
client = commands.Bot('#')

@client.event
async def on_guild_join(guild):
    with open('prefix.json','r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]




status=cycle(['s1','s2'])


@client.event
async def on_ready():

# Bot change presence
    await client.change_presence(status=discord.Status.offline,activity=discord.Game('How one get screwed?'))
    print('We have logged in as {user}')
    change_status.start()




@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello') or  message.content.startswith('HELLOp'):
        await message.channel.send('Holaaa!')

    await client.process_commands(message)

@client.command(name='ps')
async def p(ctx):
    await ctx.send(f"Hola!!  {round(client.latency * 1000)}sf")

# REPLY

@client.command(aliases=['8ball','yo'])
async def _8ball(ctx,*,question):
    response = ["As I see it", "yes Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don’t count on it",
    "It is certain",
    "It is decidedly so",
    "Most likely",
    "My reply is no",
    "My sources say no",
    "Outlook good",
    "Maybe",
    "Outlook not so good",
    "Reply hazy try again",
    "Signs point to yes",
    "Very doubtful",
    "Without a doubt"]
    await ctx.send(f"Question: {question}\n Answer :{random.choice(response)}")

### Clear

@client.command()
async def clear(ctx,amt=5):
    await ctx.channel.purge(limit=amt)


### CLEAR ERROR
@client.command()
async def cleare(ctx,amt : int):
    await ctx.channel.purge(limit=amt)

## ERROR HANDLING

# It will now only mention this error and ignore all other
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("U r Screwed :D")

@cleare.error
async def clear_error(ctx,error):
    await ctx.send("U r Screwed at max!")




### Kick Member
@client.command()
async def kick(ctx,member:discord.member,*,reason=None):
    await member.kick(reason=reason)

### BAN Account
@client.command()
async def ban(ctx, member: discord.member, *, reason=None):
    await member.ban(reason=reason)

### UnBAN
@client.command()
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    print(banned_users)
    member_name,member_discriminator=member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name,user.discriminator)==(member_name,member_discriminator ):
            await ctx.guild.unban(user)
             # await ctx.memberdm.
            await ctx.send(f'unbanned {user.mention}')
            return


### Cogs
# load commands
@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

# Unload extension
@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

# Reload extension
@client.command()
async def reload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


####    TASK

@tasks.loop(seconds=50)
async def change_status():

    await client.change_presence(activity=discord.Game(next(status)))


### Checks

@client.command()
@commands.has_permissions(manage_messages=True)
async  def cleart(ctx,amt=2):
    await ctx.channel.psurge(limit=amt)
# Only who has permisiion will be able to do it

def who(ctx):
    ctx.guild.owner_id=ctx.author.id
## creating custom check
@client.command()
@commands.check(who)
async def example(ctx):
    await ctx.send(f"Hii its {ctx.author}")




## Automatically Load all cogs
for filename in os.listdir("../../"):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run("masked")