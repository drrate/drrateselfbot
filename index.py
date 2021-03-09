#import bullshits
from discord.ext import commands
import json, time, discord, requests, random, os, asyncio

#config reading
config = open('config.json', 'r')
config = config.read()
config = json.loads(config)
print(config)

prefix = config["prefix"]
whitelist = config["whitelisted"]
token = config["token"]
embedcolor = config["embedcolor"]
print(embedcolor)
print(prefix)
print(whitelist)

print(token)
def getcolor(argument): 
    switcher = { 
            "default" : 0,
            "teal" : 0x1abc9c,
            "dark_teal" : 0x11806a,
            "green" : 0x2ecc71,
            "dark_green" : 0x1f8b4c,
            "blue" : 0x3498db,
            "dark_blue" : 0x206694,
            "purple" : 0x9b59b6,
            "dark_purple" : 0x71368a,
            "magenta" : 0xe91e63,
            "dark_magenta" : 0xad1457,
            "gold" : 0xf1c40f,
            "dark_gold" : 0xc27c0e,
            "orange" : 0xe67e22,
            "dark_orange" : 0xa84300,
            "red" : 0xe74c3c,
            "dark_red" : 0x992d22,
            "lighter_grey" : 0x95a5a6,
            "dark_grey" : 0x607d8b,
            "light_grey" : 0x979c9f,
            "darker_grey" : 0x546e7a,
            "blurple" : 0x7289da,
            "greyple" : 0x99aab5,
    }
    argument = argument.replace(' ', "_").lower()
    return switcher.get(argument, "0x2ecc71")
embedcolor = getcolor(embedcolor)
bot = commands.Bot(command_prefix=";")
@bot.event
async def on_ready():
    whitelist.append(str(bot.user.id))
    print(whitelist)
    print('ready')


@bot.event
async def on_message(message):
    author = message.author
    if str(author.id) not in whitelist:
        return
    content = message.content
    args = content.split(" ")
    command = args[0].lower().replace(prefix, "")
    args.pop(0)
    if command == "ping":
        await message.delete()
        print('e')
        before = time.monotonic()
        embedd = discord.Embed(title="Pinging..",color=embedcolor, description="Walter's Selfbot")
        message = await message.channel.send(embed=embedd)
        ping = (time.monotonic() - before) * 1000
        embeddd = discord.Embed(title=f"Pong! {int(ping)}ms",color=embedcolor, description="Walter's Selfbot")
        await message.edit(embed=embeddd)
        print(f'Ping {int(ping)}ms')
    if command == "trump":
        await message.delete()
        if len(args):
            trumpo = f"https://api.no-api-key.com/api/v2/trump?message={'%20'.join(args)}"
            r = requests.get(trumpo, allow_redirects=True)
            filename = f"trump-${random.randint(1, 500)}.png"
            open(filename, 'wb').write(r.content)
            await message.channel.send(file=discord.File(filename))
            os.remove(filename)
        else:
            trumpo = f"https://api.no-api-key.com/api/v2/trump?message=ok%20what%20should%20i%20say"
            r = requests.get(trumpo, allow_redirects=True)
            filename = f"noargs-trump-${random.randint(1, 500)}.png"
            open(filename, 'wb').write(r.content)
            await message.channel.send(file=discord.File(filename))
            os.remove(filename)
    if command == "purge":
        if args:
            try:
                limit = int(args[0])
            except:
                message.channel.send("Thats not an int lmfao", delete_after=3)
            await message.delete()
            mymessages = []
            async for m in message.channel.history():
                if len(mymessages) == limit:
                    break
                if m.author == bot.user:
                    mymessages.append('deleted some')
                    try:
                        await m.delete()
                    except:
                        print('error :flushed:')
        else:
            await message.channel.send('No Limit Gaven.', delete_after=3)
    if command == "recaptcha" or command == "captcha":
        await message.delete()
        if len(args):
            
            trump = f"https://api.no-api-key.com/api/v2/recaptcha?text={'%20'.join(args)}"
            r = requests.get(trump, allow_redirects=True)
            filename = f"recaptcha-{random.randint(1, 500)}.png"
            open(filename, 'wb').write(r.content)
            filee = discord.File(f"./{filename}", filename=filename)
            embedd = discord.Embed(color=embedcolor, description="Walter's Selfbot")
            embedd.set_image(url=f"attachment://{filename}")
            await message.channel.send(file=filee, embed=embedd)
            os.remove(filename)
        else:
            trumpo = f"https://api.no-api-key.com/api/v2/recaptcha?text=Im%20A%20Robot"
            r = requests.get(trumpo, allow_redirects=True)
            filename = f"noargs-recaptcha-${random.randint(1, 500)}.png"
            open(filename, 'wb').write(r.content)
            ilee = discord.File(f"./{filename}", filename=filename)
            embedd = discord.Embed(color=embedcolor, description="Walter's Selfbot")
            embedd.set_image(url=f"attachment://{filename}")
            await message.channel.send(file=filee, embed=embedd)
            os.remove(filename)
    if command == "avatar":
        for user in message.mentions:
            url = user.avatar_url
            if url:
                embed=discord.Embed(color=embedcolor, description="Walter's Selfbot")
                embed.set_author(name=f"user.name's Avatar")
                embed.set_thumbnail(url=url)
                await message.channel.send(embed=embed)
    if command == "spam":
        await message.delete()
        limit = int(args[0])
        args.pop(0)
        msg = " ".join(args)
        for i in range(limit + 1):
            await message.channel.send(msg)
            await asyncio.sleep(0.4)
    
    if command == "imageembed":
        if message.attachments:
            url = message.attachments[0].url
            r = requests.get(url, allow_redirects=True)
            filename = f"{random.randint(1,100)}-tmpimageembed.png"
            open(filename, 'wb').write(r.content)
        else:
            if args:
                if args[0].startswith('https://') or args[0].startswith('http://'):
                    url = args[0]
                else:
                    await message.channel.send('Please provide link/image.', delete_after=3)
                    return
            else:
                await message.channel.send('Please provide link/image.', delete_after=3)
                return
        await message.delete()
        e = discord.Embed(color=embedcolor)
        e.set_image(url=url)    
        await message.channel.send(embed=e)
        os.remove(filename)

bot.run(token, bot=False)