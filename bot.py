import discord, asyncio
from discord.ext import commands
from discord.ext.commands import *

http = discord.http
bot = commands.Bot(command_prefix='¤')

@bot.event
async def on_ready():
    await discord.Client.change_presence(bot, game=discord.Game(name='dead'), status=discord.Status.dnd)
    print("Ready..?")
    print(bot.user.name)
    print(bot.user.id)

@bot.command(pass_context=True)
async def boi(ctx):
    await bot.delete_message(ctx.message)
    await bot.say('🅱oi')

@bot.command(pass_context=True)
async def deletdis(ctx):
    await bot.say('Deleting message in 3...')
    await asyncio.sleep(1)
    await bot.say('2...')
    await asyncio.sleep(1)
    await bot.say('1...')
    await asyncio.sleep(1)
    await bot.say('Poof!')
    await bot.delete_message(ctx.message)

@bot.command()
async def doge():
    embed = discord.Embed()
    embed.set_image(url='http://i0.kym-cdn.com/entries/icons/original/000/013/564/doge.jpg')
    await bot.say(embed=embed)

@bot.command()
async def echo(message: str):
    await bot.say(message)

@bot.command()
async def ping():
    await bot.say('Pong!')

@bot.command(pass_context=True)
async def react(ctx):
    await bot.add_reaction(ctx.message, '\N{THUMBS UP SIGN}')

@bot.command(pass_context=True)
async def bot_space(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    msg = message.replace("", " ")
    msg = msg.replace("* ", "*")
    msg = msg.replace("_ ", "_")
    msg = msg.replace("~ ", "~")
    await bot.say(msg)

@bot.command(pass_context=True)
async def space(ctx, *, message: str):
    a = ctx.message.author
    await bot.delete_message(ctx.message)
    msg = message.replace("", " ")
    msg = msg.replace("* ", "*")
    msg = msg.replace("_ ", "_")
    msg = msg.replace("~ ", "~")
    await bot.say(str(a) + ' has something important to tell you:')
    await bot.say(msg)



bot.run("NDE4NTQwOTYxNzk1Mjc2ODAx.DXjGQg.Fq5BjMeP6KY55LPB_Q_2EtgGJag")