from discord.ext import commands
from utils import default

import asyncio


class Fun_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command()
    async def echo(self, ctx, *, text: str):
        """
        Whatever you say!
        """
        t_echo = text.replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"{t_echo}")

    @commands.command()
    async def say(self, ctx, *, text: str):
        """
        Whatever you say!
        """
        await ctx.message.delete()
        t_echo = text.replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"{t_echo}")

    @commands.command(hidden=True)
    async def cinder(self, ctx):
        """
        xd
        """
        await ctx.message.delete()
        await ctx.send("Cinder is gay. That's why he's called daddy.")

    @commands.command(hidden=True)
    async def fare(self, ctx):
        """
        xd
        """
        await ctx.message.delete()
        await ctx.send("Fare is bigger gay than Cinder.")

    @commands.command(hidden=True)
    async def paws(self, ctx):
        """
        xd
        """
        await ctx.message.delete()
        await ctx.send("Paws is mommy.")

    @commands.command(hidden=True)
    async def stultus(self, ctx):
        """
        xd
        """
        await ctx.message.delete()
        await ctx.send("Stultus the sultana!")

    @commands.command()
    async def poll(self, ctx, time, *, question):
        """
        Creates a poll
        """
        await ctx.message.delete()
        time = int(time)
        pollmsg = await ctx.send(
            f"{ctx.message.author.mention} created a poll that will end after {time} seconds!\n**{question}**\n\nReact with :thumbsup: or :thumbsdown: to vote!"
        )
        await pollmsg.add_reaction("👍")
        await pollmsg.add_reaction("👎")
        await asyncio.sleep(time)
        reactiongrab = await ctx.channel.get_message(pollmsg.id)
        for reaction in reactiongrab.reactions:
            if reaction.emoji == str("👍"):
                upvote_count = reaction.count
            else:
                if reaction.emoji == str("👎"):
                    downvote_count = reaction.count
                else:
                    pass
        await pollmsg.edit(
            content=f"{ctx.message.author.mention} created a poll that will end after {time} seconds!\n**{question}**\n\nTime's up!\n👍 = {upvote_count-1}\n\n👎 = {downvote_count-1}"
        )
        await ctx.send(
            f"**{question}**\n\nTime's up!\n👍 = {upvote_count-1}\n\n👎 = {downvote_count-1}"
        )


def setup(bot):
    bot.add_cog(Fun_Commands(bot))
