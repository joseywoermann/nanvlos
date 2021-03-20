import discord
from discord.ext import commands
import logging

from github import Github
from pprint import pprint

class MakeIssue(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['issue', 'createissue', 'report', 'makebugreport', 'bugreport'])
    @commands.guild_only()
    async def makeissue(self, ctx, pTitle, pBody = None):
        async with ctx.channel.typing():
            with open('github.TOKEN','r') as file:
                TOKEN = file.read()

            g = Github(TOKEN)
            repo = g.get_repo("joseywoermann/navnlos")

            if pBody:
                i = repo.create_issue(
                    title=pTitle,
                    body = pBody + " (Issue created by Discord-User `" + str(ctx.author) + "`)",
                    assignee="joseywoermann",
                )
            else:
                i = repo.create_issue(
                    title=pTitle,
                    body = "(Issue created by Discord-user `" + str(ctx.author) + "`)",
                    assignee="joseywoermann",
                )

            issue_embed = discord.Embed(title = "Bugreport gesendet!", description = "[Alle Bugreports](https://github.com/joseywoermann/navnlos/issues)")
            issue_embed.set_footer(text = "$bugreport | @navnløs")
            logging.info(str(ctx.author) + " created an issue.")
        await ctx.reply(content = None, embed = issue_embed)


def setup(client):
    client.add_cog(MakeIssue(client))
