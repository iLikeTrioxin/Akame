# bot.py
import os

import discord
import nekos
from discord.ext import commands
from random import randrange
from threading import Lock
import asyncio

# defines token for discord
import credentials.py

bot = commands.Bot(command_prefix='#')

cClients = []
tags = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron', 'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar', 'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo', 'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg', 'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif', 'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof']

resultImg = []
async def getImg(tag):
    img = nekos.img(tag)
    with lock:
        resultImg.append(img)

@bot.command(name='wojciechowski')
async def wojciechowski(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/786935531438473286/820769130357456906/unknown.png")

@bot.command(name='xd')
async def xd(ctx):
    connected = ctx.author.voice
    if connected:
        await connected.channel.connect()
        
@bot.command(name='do')
async def do(ctx, msg):
    connected = ctx.author.voice
    if(msg=="add"):
        print("trying to add...")
        cll = discord.Client()
        vcll = discord.VoiceClient(client=cll, channel=connected)
        await connected.channel.connect(cls=vcll)
        for mem in connected.channel.members:
            print(mem.nick)
        print("done")
        
@bot.command(name='ale')
async def xd(ctx, msg=" "):
    omsg = "ale co?"
    
    if msg in ["sex", "seks", "segz"]:
        omsg = "jes, inded"
        
    await ctx.send(omsg)

@bot.command(name='i')
async def i(ctx, tag='random', x="1"):
    print("requested " + tag)
    tag = tag.lower()
    
    random = (tag == "random")
    
    if (int(x) > 100):
        ctx.send("max number of messeges per command is 100.")
        return
    
    tasks = []
    
    if (random):
        tasks = [nekos.img(tags[ randrange(0, len(tags) - 1) ]) for i in range(0, int(x))]
    else:
        tasks = [nekos.img(tag) for i in range(0, int(x))]
    print("requested "+str(int(x))+" images.")
    #await asyncio.gather(*tasks)
    #print("generated "+str(len(resultImg))+" images.")
    resultImg = tasks
    msgs = [""]
    cMsg = 0
    for img in resultImg:
        print("msg lenght = "+str(len(msgs[cMsg]) + len(img) + 1))
        if((len(msgs[cMsg]) + len(img) + 3) >= 250):
            print("created new msg")
            msgs.append("")
            cMsg += 1
        msgs[cMsg] += (' ' + img)
    
    tasks = [ ctx.send( msg ) for msg in msgs ]
    
    asyncio.gather(*tasks)


@bot.command(name='h')
async def h(ctx, tag='neko'):
    print("requested "+tag)
    #guild = ctx.guild
    #existing_channel = discord.utils.get(guild.channels, name=channel_name)
    msg = ""
    msg += "For now avalible tags are:\n"
    
    for tag in tags:
        msg+=("-"+tag+"\n")
        
    await ctx.send(msg)

bot.run(TOKEN)
