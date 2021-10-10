from discord     import Client, VoiceClient
from discord.ext import commands
from nekos       import img
from random      import randrange

# defines TOKEN for discord
from credentials import TOKEN

bot = commands.Bot(command_prefix='#')

cClients = []
tags = ['feet'             , 'yuri' , 'trap', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les',
        'wallpaper'        , 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron', 'cum_jpg', 'bj',
        'nsfw_neko_gif'    , 'solo', 'kemonomimi', 'nsfw_avatar', 'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar',
        'erofeet'          , 'holo', 'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg', 'pwankg', 'classic',
        'kuni'             , 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs',
        'random_hentai_gif', 'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof']


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
    if msg == "add":
        print("trying to add...")
        cll = Client()
        voiceClient = VoiceClient(client=cll, channel=connected)
        await connected.channel.connect(cls=voiceClient)
        for mem in connected.channel.members:
            print(mem.nick)
        print("done")


bulas = [
    [
        'https://cdn.discordapp.com/attachments/752997029021745172/896085639047577660/20747972_1842000032795410_503458318229837137_o.png',
        'Dobrakowska says jes to that idea'
    ],
    [
        'https://media.discordapp.net/attachments/755531580721594460/896087649184538634/image0.jpg?width=346&height=646',
        'Kociuga feels this too'
    ],
    [
        'https://media.discordapp.net/attachments/755531580721594460/896087700191465472/image2.jpg?width=346&height=646',
        'Cowboy said jes'
    ]
]


@bot.command(name='bula')
async def bula(ctx):
    bulaid = randrange(0, len(bulas))
    await ctx.send(bulas[bulaid][0])
    await ctx.send(bulas[bulaid][1])


@bot.command(name='ale')
async def xd(ctx, msg=" "):
    omsg = "ale co?"

    if msg in ["sex", "seks", "segz"]:
        omsg = "jes, indeed"

    await ctx.send(omsg)


@bot.command(name='gimme')
async def i(ctx, tag='random'):
    tag = tag.lower()

    if tag == "random":
        tag = tags[randrange(0, len(tags))]

    if tag not in tags:
        await ctx.send("This tag is not available.")
        return;

    await ctx.send(img(tag))


@bot.command(name='h')
async def h(ctx):
    msg = ""
    msg += "For now available tags are:\n"

    for tag in tags:
        msg += ("-" + tag + "\n")

    await ctx.send(msg)


bot.run(TOKEN)
