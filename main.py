from discord     import Client, VoiceClient
from discord.ext import commands
from nekos       import img
from random      import randrange
from datetime    import datetime
from json        import loads, dumps
from os          import mkdir
from mysql       import connector

# defines TOKEN, DB_USERNAME and DB_PASSWORD
from credentials import TOKEN

bot = commands.Bot(command_prefix='#')

dbConnection = connector.connect(
    host     = '127.0.0.1',
    user     = DB_USERNAME,
    password = DB_PASSWORD
)

async def checkServer(name: str):
    dbCursor = dbConnection.cursor()
    dbName   = name.replace(' ', '_')
    dbCursor.execute("CREATE DATABASE IF NOT EXISTS {dbName}; USE {dbName};")


@bot.event
async def on_message(msg):
    checkServer("")
    await bot.process_commands(msg)


tags = ['lewdkemo'         , 'holoero', 'solog' , 'tits' , 'poke', 
        'hololewd'         , 'erofeet', 'spank' , 'feet' , 'anal', 
        'fox_girl'         , 'blowjob', 'pussy' , 'woof' , 'slap', 
        'futanari'         , 'erokemo', 'lewdk' , 'ngif' , 'baka', 'bj'  , 
        'pussy_jpg'        , 'eroyuri', 'waifu' , 'eron' , 'holo', 'cum' , 
        'wallpaper'        , 'cum_jpg', 'boobs' , 'yuri' , 'keta', 'pat' , 
        'smallboobs'       , 'classic', 'goose' , 'trap' , 'solo', 'les' , 
        'kemonomimi'       , 'avatar' , 'feetg' , 'gecg' , 'kuni', 'ero' , 
        'nsfw_avatar'      , 'pwankg' , 'cuddle', 'feed' , 'smug', 'hug' , 
        'nsfw_neko_gif'    , 'hentai' , 'tickle', 'lewd' , 'kiss', 'erok', 
        'random_hentai_gif', 'lizard' , 'femdom', '8ball', 'neko', 'gasm' ]


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
dbConnection.close()
