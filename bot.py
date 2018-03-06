import asyncio, config, discord
from discord.ext import commands
from discord.ext.commands import *

bot = commands.Bot(command_prefix='¤')
bot.remove_command('help')

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

@bot.command()
async def commands():
    embed=discord.Embed(title="Commands", color=0x0ff3ff)
    embed.add_field(name="Just about everything", value="boi, commands, deletdis [msg], doge, dothething, echo [msg], memelicious [msg], ping, react, bot_space [msg], space [msg]", inline=False)
    await bot.say(embed=embed)

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
    embed = discord.Embed(color = 0xffde78)
    embed.set_image(url='http://i0.kym-cdn.com/entries/icons/original/000/013/564/doge.jpg')
    await bot.say(embed=embed)

@bot.command()
async def dothething():
    await bot.say('*tips fedora*')
    await bot.say("***M ' L A D Y***")

@bot.command()
async def echo(message: str):
    await bot.say(message)

@bot.command(name='help')
async def _help():
    await bot.say('***HALP IZ DED***')
    await bot.say('***HALP URSLEF***')
    await bot.say('*(or use ¤commands idc)*')

@bot.command(pass_context=True)
async def memelicious(ctx, *, message: str):
    await bot.delete_message(ctx.message)
    msg = message.replace("", " ")
    await bot.say("***" + msg.upper().strip(' ') + "***")

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



<<<<<<< HEAD
bot.run(config.token)
=======
bot.run(token)
>>>>>>> 160d81c9961711cb82fe6491ecfb9c19900e388c
