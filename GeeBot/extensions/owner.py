from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
from contextlib import redirect_stdout
import io
import re
import shutil
from platform import python_version
import gc

# to expose to the eval command
import datetime
from collections import Counter

class Admin:

    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()

    def cleanup_code(self, content):
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])
        return content.strip('` \n')


    async def __local_check(self, ctx):
        if ctx.author.id == 213959844212899841:
            return True
        else:
            return

		
    @commands.command(pass_context=True, hidden=True, name='eval', aliases=['evaluate'])
    async def _eval(self, ctx, *, body: str):
        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'
        await ctx.message.add_reaction('a:loading:462623304503656448')
        

        await asyncio.sleep(2)
        try:
            exec(to_compile, env)
        except Exception as e:
            await ctx.message.remove_reaction('a:loading:462623304503656448', member=ctx.me)
            await ctx.message.add_reaction('finished:462624893683499008')
            fooem = discord.Embed(color=0xFF6A00)
            fooem.add_field(name="Code evaluation was not successful.", value=f'```\n{e.__class__.__name__}: {e}\n```')
            fooem.set_footer(text=f"Evaluated using Python {python_version()}", icon_url="http://i.imgur.com/9EftiVK.png")
            fooem.timestamp = ctx.message.created_at
            return await ctx.send(embed=fooem)

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.message.remove_reaction('a:loading:462623304503656448', member=ctx.me)
            await ctx.message.add_reaction('a:NeeNoo:453584890227589120')
            fooem = discord.Embed(color=0xFF6A00)
            fooem.add_field(name="Code evaluation was not successful.", value=f'```py\n{value}{traceback.format_exc()}\n```')
            fooem.set_footer(text=f"Evaluated using Python {python_version()}", icon_url="http://i.imgur.com/9EftiVK.png")
            fooem.timestamp = ctx.message.created_at
            await ctx.send(embed=fooem)
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.remove_reaction('a:loading:462623304503656448', member=ctx.me)
                await ctx.message.add_reaction('finished:462624893683499008')
            except:
                pass

            if ret is None:
                if value:
                    sfooem = discord.Embed(color=0xFF6A00)
                    sfooem.add_field(name="Code evaluation was successful!", value=f'```py\n{value}\n```')
                    sfooem.set_footer(text=f"Evaluated using Python {python_version()}", icon_url="http://i.imgur.com/9EftiVK.png")
                    sfooem.timestamp = ctx.message.created_at
                    await ctx.send(embed=sfooem)
            else:
                self._last_result = ret
                ssfooem = discord.Embed(color=0xFF6A00)
                ssfooem.add_field(name="Code evaluation was successful!", value=f'```py\n{value}{ret}\n```')
                ssfooem.set_footer(text=f"Evaluated using Python {python_version()}", icon_url="http://i.imgur.com/9EftiVK.png")
                ssfooem.timestamp = ctx.message.created_at
                await ctx.send(embed=ssfooem)

    @commands.command(hidden=True, aliases=['die'])
    async def logout(self, ctx):
        embed = discord.Embed(color=0xFF6A00)
        embed.add_field(name='Naoko logout', value="I've successfully logged out from Discord.")
        embed.set_footer(
            text='Command requested by {}'.format(ctx.author),
            icon_url='https://raw.githubusercontent.com/F4stZ4p/resources-for-discord-bot/master/key.ico')
        await ctx.channel.send(embed=embed)
        await self.bot.logout()

    @commands.command(hidden=True, aliases=['rmc'])
    async def rmcache(self, ctx):
        shutil.rmtree('__pycache__')
        embed = discord.Embed(color=0xFF6A00)
        embed.set_footer(text='Cache cleared.', icon_url='https://raw.githubusercontent.com/F4stZ4p/resources-for-discord-bot/master/tick.ico')
        await ctx.send(embed=embed)
		
		
    @commands.command(hidden=True, aliases=["say","print"])
    async def echo(self, ctx, *, content):
        await ctx.send(content)

    @commands.command(pass_context=True, aliases=["st"], hidden=True)
    async def sendtyping(self, ctx):
        await ctx.message.add_reaction('a:loading:462623304503656448')
        await ctx.trigger_typing()
        await asyncio.sleep(10)
        await ctx.message.remove_reaction('a:loading:462623304503656448', member=ctx.me)
        await ctx.message.add_reaction('finished:462624893683499008')
		
    @commands.command(pass_context=True, hidden=True)
    async def speedup(self, ctx):
        await ctx.message.add_reaction('a:loading:462623304503656448')
        gc.collect()
        del gc.garbage[:]
        await ctx.message.remove_reaction('a:loading:462623304503656448', member=ctx.me)
        await ctx.message.add_reaction('finished:462624893683499008')

def setup(bot):
    bot.add_cog(Admin(bot))