import time
import discord
from discord.ext import commands
import asyncio
import aiohttp
import random
from pyfiglet import Figlet

message = discord.MessageType
bot = commands.Bot(command_prefix='G')

class Fun():
    	def __init__(self, bot):
            self.bot = bot
            self.emoji_true = "🔵"
            self.emoji_false = "🔴"
            self.session = aiohttp.ClientSession(loop=self.bot.loop)
            self.tags = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk', 'ngif', 'meow', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron', 'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar', 'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo', 'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg', 'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'Random_hentai_gif', 'smallboobs', 'hug', 'ero']

            @bot.command()
            async def avatar(ctx, user : discord.User):
                embed = discord.Embed(color=0xFF6A00, url=user.avatar_url)
                embed.set_image(url=user.avatar_url)
                embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)

            @bot.command(aliases=["hb"])
            async def hastebin(ctx, *, content):
                async with aiohttp.ClientSession() as session:
                    async with session.post("https://hastebin.com/documents",data=content.encode('utf-8')) as post:
                        post = await post.json()
                        hasteurl = f"https://hastebin.com/{post['key']}"
                        embed = discord.Embed(title="Link to hastebin", url=hasteurl, color=0xFF6A00)
                        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
                        await ctx.send(embed=embed)
                        print (str(ctx.author) + "created a hastebin link: https://hastebin.com/{post['key']}" + time.ctime())
            
            @bot.command()
            async def neko(ctx):
                async with aiohttp.ClientSession() as cs:
                    async with cs.get('https://nekos.life/api/v2/img/neko') as r:
                        res = await r.json()
                        embed = discord.Embed(color=0xFF6A00)
                        embed.set_image(url=res['url'])
                        await ctx.send(embed=embed)
                        print (str(ctx.author) + 'used the Neko command at ' + time.ctime())

            @bot.command()
            async def shibe(ctx):
                async with aiohttp.ClientSession() as cs:
                    async with cs.get('http://shibe.online/api/shibes?count=[1]&urls=[true/false]&httpsUrls=[true/false]') as r:
                        res = await r.json()
                        embed = discord.Embed(color=0xFF6A00)
                        embed.set_image(url=str(res).strip("[']"))
                        await ctx.send(embed=embed)
                        print (str(ctx.author) + 'used the Shibe command at ' + time.ctime())

            @bot.command(aliases=["cooltext", "3d", "textart"])
            async def ascii(ctx, *, text):
                try:
                    await ctx.send(f"```fix\n{Figlet(font='slant').renderText(text)}```")
                except Exception:
                    await ctx.send("<a:NeeNoo:453584890227589120> **Too long to send.** <a:NeeNoo:453584890227589120>")


def setup(bot):
	bot.add_cog(Fun(bot))

