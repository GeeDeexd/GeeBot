import time
import discord
from discord.ext import commands
import asyncio
import random
import aiohttp
import random


startup_extensions = ['extensions.owner', 'extensions.fun', 'extensions.moderator']
message = discord.MessageType
description = '''I am GeeBot, my creator is GeeDee#2774 and my main discord server is https://discord.gg/ccrY87j! I got lots of help from chr1s#7185!'''
bot = commands.Bot(command_prefix='G', description=description)

@bot.event
async def on_ready():
        await bot.change_presence(activity=discord.Streaming(name="Ghelp", url="https://twitch.tv/kvantumgt"))
        print('###########################################################')
        print('Version: ', discord.__version__)
        print('Up and running since', time.ctime(), '!')
        print('Logged in as', bot.user.name)
        print('ID:', bot.user.id)
        print('###########################################################')

@bot.check
async def bprotect(ctx):
    if ctx.author.bot:
        await ctx.send(":x: **Permission denied. Bots like you can't execute my commands.**", delete_after=5)
        return
    else:
        return True

@bot.event
async def on_message(message):
    if message.content.upper() == "PING":
        await message.channel.send('Pong')
        print (str(message.author) + " pinged the bot at " + time.ctime())
    if message.content.upper() == ('9111'):
        await message.channel.send(file=discord.File("C:\\GeeBot\\Development\\Resources\\9111.gif"))
        print (str(message.author) + ' called the mega police at ' + time.ctime())
    if message.content.startswith('GUYS'):
        await message.channel.send('Lads*')

    await bot.process_commands(message)


@bot.command()
@commands.has_any_role("Moderators")
async def plsgiverole(ctx, roles):
    a = discord.utils.get(ctx.guild.roles, name=roles)
    await ctx.author.add_roles(a)

@bot.command(description='For when you wanna settle the score some other way')
async def pick(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

if True:
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


bot.run('token')

