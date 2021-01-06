import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print('봇 실행 완료')

@bot.command()
async def 청소(ctx, amount=999):
    await ctx.channel.purge(limit=amount)

bot.run('Nzk1NDczODQ3OTg1MzczMjE0.X_J4wA.KtpcyTrfBQITtQw_cS6aBvpPdPE')