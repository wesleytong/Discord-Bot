import discord
import asyncio
import random
import botToken
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
intents = discord.Intents.all()
disc = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'), description=description, intents=intents)
print(discord.__version__)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


# @bot.event
# async def on_typing(channel,msg, when):
#     await channel.send('Stop typing')

@bot.event
async def on_message(message):

    await bot.process_commands(message)


# @bot.command()
# async def clear(ctx, amount: int):
#     await ctx.channel.purge(limit=1)
#     f = open('deletedTxts.txt', 'a')
#     async for message in ctx.channel.history(limit=amount):
#         f.write(message.content)
#         f.write('\n')
#     f.close()
#     await ctx.channel.purge(limit=amount)
#     await ctx.send('Done!', delete_after=5)

@bot.command()
async def roulette(ctx, bet, amount):
    winning = random.randint(0,1)
    embedded = discord.Embed()
    if winning == 0 and bet == 'black':
        embedded.add_field
    await ctx.send('yeet')


bot.run(botToken.token)
