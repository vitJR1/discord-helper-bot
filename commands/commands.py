import discord

from cfg.config import HELP_STRING

from discord.ext import commands

from commands.title.title import Title

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

bot.remove_command('help')


@bot.command()
async def help(ctx):
    await ctx.send(HELP_STRING)

@bot.command()
async def title(ctx, str, level = 3):
    await ctx.send(Title(str, level))

