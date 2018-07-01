import time
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='G')

class moderator:
    def __init__(self, bot):

        @bot.command()
        @commands.has_permissions(kick_members=True)
        async def kick(ctx, user: discord.Member):
            await ctx.send("DAAAAM **{}** GOT **KICKED** LMFAO".format(user.name))
            await ctx.kick(user)
            print (str(ctx.author) + 'kicked {} at ' + time.ctime())

        @bot.command()
        @commands.has_permissions(ban_members=True)
        async def ban(ctx, user: discord.Member):
            await ctx.send("DAAAAM **{}** GOT **BANNED** AND HE PROBS AIN'T COMING BACK LMFAO".format(user.name))
            await ctx.ban(user)
            print (str(ctx.author) + 'banned {} at ' + time.ctime())


def setup(bot):
    bot.add_cog(moderator(bot))