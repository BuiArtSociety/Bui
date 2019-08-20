from discord.ext import commands
from utils import default

import asyncio
import discord


class Role_Distribution(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.group()
    async def iam(self, ctx):
        """
        Used for assigning roles to yourself!
        """
        if ctx.invoked_subcommand is None:
            _help = await ctx.bot.formatter.format_help_for(ctx, ctx.command)

            for page in _help:
                await ctx.send(page)

    @iam.command(name="nsfw")
    async def iam_nsfw(self, ctx):
        """
        - Gives the NSFW role
        """

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "👍"

        await ctx.message.delete()
        try:
            msg = await ctx.author.send(
                f"**{ctx.author.name}**, by requesting this role, you are agreeing to our terms and conditions, Discord's Terms of Service, and Community Guideline. We are not liable if you are found that you are not within legal age to view NSFW content within your country.\n\nOur Terms of Service : <https://goo.gl/Mi4yEj>\nDiscord's Terms of Service: <https://discordapp.com/terms>\nDiscord's Community Guidelines: <https://discordapp.com/guidelines>\n\nIf you agree by all of the above, then please react with :thumbsup: below."
            )
        except discord.Forbidden:
            await ctx.send(f"I can't send messages to you, {ctx.author.name}!")
        await msg.add_reaction("👍")
        try:
            reaction, user = await self.bot.wait_for(
                "reaction_add", timeout=60.0, check=check
            )
        except asyncio.TimeoutError:
            await ctx.author.send("Timed out..")
            await msg.delete()
        else:
            dmmsg = await ctx.author.send(
                "You should have the NSFW role now! If not, contact a staff member."
            )
            await msg.delete()
            message = []
            for role in ctx.guild.roles:
                if role.name == "NSFW":
                    message.append(role.id)
            try:
                therole = discord.Object(id=message[0])
            except:
                return

            await ctx.author.add_roles(therole)
            await asyncio.sleep(5)
            await dmmsg.delete()

    @iam.command(name="advertising")
    async def iam_advertising(self, ctx):
        """
        - Gives the Advertising role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Advertising":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.add_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have given you the **Advertising** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iam.command(name="drawpile")
    async def iam_drawpile(self, ctx):
        """
        - Gives the Drawpile role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Drawpile":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.add_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have given you the **Drawpile** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iam.command(name="artpg")
    async def iam_artpg(self, ctx):
        """
        - Gives the ArtPG role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "ArtPG":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.add_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have given you the **ArtPG** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iam.command(name="event")
    async def iam_event(self, ctx):
        """
        - Gives the Event role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Event":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.add_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have given you the **Event** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iam.command(name="sketchdaily")
    async def iam_sketchdaily(self, ctx):
        """
        - Gives the Sketchdaily role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Sketchdaily":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.add_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have given you the **Sketchdaily** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iam.command(name="artist")
    async def iam_artist(self, ctx):
        """
        - Gives the Artist role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Artist":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.add_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have given you the **Artist** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iam.command(name="producer")
    async def iam_producer(self, ctx):
        """
        - Gives the Producer role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Producer":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.add_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have given you the **Producer** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iam.command(name="writer")
    async def iam_writer(self, ctx):
        """
        - Gives the Writer role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Writer":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.add_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have given you the **Writer** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @commands.group()
    async def iamnot(self, ctx):
        """
        Used for un-assigning roles to yourself!
        """
        if ctx.invoked_subcommand is None:
            _help = await ctx.bot.formatter.format_help_for(ctx, ctx.command)

            for page in _help:
                await ctx.send(page)

    @iamnot.command(name="nsfw")
    async def iamnot_nsfw(self, ctx):
        """
        - Removes the NSFW role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "NSFW":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.remove_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have removed you from the **NSFW** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iamnot.command(name="advertising")
    async def iamnot_advertising(self, ctx):
        """
        - Removes the Advertising role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Advertising":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.remove_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have removed you from the **Advertising** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iamnot.command(name="drawpile")
    async def iamnot_drawpile(self, ctx):
        """
        - Removes the Drawpile role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Drawpile":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.remove_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have removed you from the **Drawpile** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iamnot.command(name="artpg")
    async def iamnot_artpg(self, ctx):
        """
        - Removes the ArtPG role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "ArtPG":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.remove_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have removed you from the **ArtPG** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iamnot.command(name="event")
    async def iamnot_event(self, ctx):
        """
        - Removes the Event role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Event":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.remove_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have removed you from the **Event** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iamnot.command(name="sketchdaily")
    async def iamnot_sketchdaily(self, ctx):
        """
        - Removes the Sketchdaily role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Sketchdaily":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.remove_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have removed you from the **Sketchdaily** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iamnot.command(name="artist")
    async def iamnot_artist(self, ctx):
        """
        - Removes the Artist role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Artist":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.remove_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have removed you from the **Artist** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iamnot.command(name="producer")
    async def iamnot_producer(self, ctx):
        """
        - Removes the Producer role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Producer":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.remove_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have removed you from the **Producer** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

    @iamnot.command(name="writer")
    async def iamnot_writer(self, ctx):
        """
        - Removes the Writer role
        """

        message = []
        for role in ctx.guild.roles:
            if role.name == "Writer":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except:
            return

        await ctx.author.remove_roles(therole)
        await ctx.message.delete()
        msg = await ctx.send(
            f"**{ctx.author.name}**, I have removed you from the **Writer** role!"
        )
        await asyncio.sleep(5)
        await msg.delete()

def setup(bot):
    bot.add_cog(Role_Distribution(bot))
