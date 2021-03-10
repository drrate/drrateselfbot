

print(" __      __        .__   __              /\\          _________      .__   ________.           __   ")
print("/  \\    /  \\_____  |  |_/  |_  __________)/ ______  /   _____/ ____ |  |_/ ____\\_ |__   _____/  |_ ")
print("\\   \\/\\/   /\\__  \\ |  |\\   __\\/ __ \\_  __ \\/  ___/  \\_____  \\_/ __ \\|  |\\   __\\ | __ \\ /  _ \\   __\\")
print(" \\        /  / __ \\|  |_|  | \\  ___/|  | \\/\\___ \\   /        \\  ___/|  |_|  |   | \\_\\ (  <_> )  |  ")
print("  \\__/\\  /  (____  /____/__|  \\___  >__|  /____  > /_______  /\\___  >____/__|   |___  /\\____/|__|  ")
print("       \\/        \\/               \\/           \\/          \\/     \\/                \\/             ")


#import bullshits
from discord.ext import commands
import json, time, discord, requests, random, os, asyncio, subprocess, platform

#config reading
config = open('config.json', 'r')
config = config.read()
config = json.loads(config)
print(config)

prefix = config["prefix"]
whitelist = config["whitelisted"]
token = config["token"]
embedcolor = config["embedcolor"]

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
    return switcher.get(argument, "")
if config["randomcolor"] == "true":
    randomizecolor = True
else:
    randomizecolor = False
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
    if content.startswith(prefix):
        pass
    else:
        return
    if command == "ping":
        await message.delete()
        print('e')
        before = time.monotonic()
        if randomizecolor:
            embedd = discord.Embed(title="Pinging..",color=discord.Color.random(), description="Walter's Selfbot")
        else:
            embedd = discord.Embed(title="Pinging..",color=embedcolor, description="Walter's Selfbot")
        message = await message.channel.send(embed=embedd)
        ping = (time.monotonic() - before) * 1000
        if randomizecolor:
            embeddd = discord.Embed(title=f"Pong! {int(ping)}ms",color=discord.Color.random(), description="Walter's Selfbot")
        else:
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
            if randomizecolor:
                embedd = discord.Embed(color=discord.Color.random(), description="Walter's Selfbot")
            else:
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
            if randomizecolor:
                embedd = discord.Embed(color=discord.Color.random(), description="Walter's Selfbot")
            else:
                embedd = discord.Embed(color=embedcolor, description="Walter's Selfbot")
            embedd.set_image(url=f"attachment://{filename}")
            await message.channel.send(file=filee, embed=embedd)
            os.remove(filename)
    if command == "avatar":
        if message.mentions:
            for user in message.mentions:
                url = user.avatar_url
                if url:
                    if randomizecolor:
                        embedd = discord.Embed(color=discord.Color.random(), description="Walter's Selfbot")
                    else:
                        embedd = discord.Embed(color=embedcolor, description="Walter's Selfbot")
                    embedd.set_author(name=f"{message.mentions[0].name}'s Avatar")
                    embedd.set_thumbnail(url=url)
                    await message.channel.send(embed=embedd)
        else:
            url = bot.user.avatar_url
            if randomizecolor:
                embedd = discord.Embed(color=discord.Color.random(), description="Walter's Selfbot")
            else:
                embedd = discord.Embed(color=embedcolor, description="Walter's Selfbot")
            embedd.set_author(name=f"{bot.user.name}'s Avatar")
            embedd.set_thumbnail(url=url)
            await message.channel.send(embed=embedd)
    if command == "spam":
        await message.delete()
        limit = int(args[0])
        args.pop(0)
        msg = " ".join(args)
        for i in range(limit + 1):
            await message.channel.send(msg)
            await asyncio.sleep(0.4)
    
    if command == "imageembed":
        if args:
            if args[0].startswith('https://') or args[0].startswith('http://'):
                url = args[0]
            else:
                await message.channel.send('Please provide link.', delete_after=3)
                return
        else:
            await message.channel.send('Please provide link.', delete_after=3)
            return
        await message.delete()
        
        if randomizecolor:
            embedd = discord.Embed(color=discord.Color.random(), description="Walter's Selfbot")
        else:
            embedd = discord.Embed(color=embedcolor, description="Walter's Selfbot")
        embedd.set_image(url=url)    
        await message.channel.send(embed=embedd)
        
        
    if command == "embed":
        await message.delete()
        t = " ".join(args).split(",")
        if len(t) == 1:
            if randomizecolor:
                e = discord.Embed(color=discord.Color.random(), description=t[0])
            else:
                e = discord.Embed(color=embedcolor,description=t[0])
            
            await message.channel.send(embed=e)
        elif len(t) == 2 or len(t) > 2:
            if randomizecolor:
                e = discord.Embed(color=discord.Color.random(), title=t[0], description=t[1])
            else:
                e = discord.Embed(color=embedcolor, title=t[0], description=t[1])
            
            await message.channel.send(embed=e)
    if command == 'ghostping':
        await message.delete()
        limit = int(args[0])
        args.pop(0)
        if "--id" in content:
            content = content.replace('--id', "")
            msg = f"<@!{args[0]}>"
        else:
            msg = " ".join(args)
        for i in range(limit):
            await message.channel.send(msg, delete_after=0.3)
            await asyncio.sleep(0.4)
    if command == "help":
        await message.delete()
        if randomizecolor:
            embed = discord.Embed(color=discord.Color.random(), description="Prefix: {prefix} | Walter's selfbot - https://github.com/ProYT303/walterselfbot")
        else:
            embed = discord.Embed(color=embedcolor, description="Prefix: {prefix} | Walter's selfbot - https://github.com/ProYT303/walterselfbot")
        embed.add_field(name="ping", value="Measure your ping! ", inline=False)
        embed.add_field(name="trump", value="Trump said pog :flushed:", inline=True)
        embed.add_field(name="purge", value="Purge your messages!", inline=True)
        embed.add_field(name="recaptcha", value="Ahh, that annoying captcha..", inline=False)
        embed.add_field(name="avatar", value="The title said it all.", inline=True)
        embed.add_field(name="spam", value="Usage : <limit> <message>, ps: will spam on the channel you send in.", inline=True)
        embed.add_field(name="imageembed", value="The title said it all. use links.", inline=True)
        embed.add_field(name="embed", value="Usage : <Title> <desc>.", inline=True)
        embed.add_field(name="ghostping", value="Usage : <limit> <message> / <limit> --id <userid>", inline=True)
        embed.add_field(name="ascii", value="Generates graffiti ascii art.", inline=True)

        await message.channel.send(embed=embed)            
    if command == "ascii":
        await message.delete()
        
        a = "+".join(args)
        b = f"https://artii.herokuapp.com/make?text={a}&font=graffiti"
        r = requests.get(b, allow_redirects=True)
        asci = f"```{r.content.decode('utf8')}```"
        if len(a) < 11:
            if randomizecolor:
                e = discord.Embed(color=discord.Color.random())
            else:
                e = discord.Embed(color=embedcolor)
            e.add_field(name="Ascii Generated!", value=asci, inline=False)
            await message.channel.send(embed=e)
        else:
            await message.channel.send(asci)
    if command == "deepfry":
        if message.attachments:
            
            url = message.attachements[0].url
        if message.mentions:
            url = message.mentions[0].avatar_url
        else:
            if args:
                url = args[0]
            else:
                await message.channel.send('Please put a image/url', delete_after=2)
        b = f"https://nekobot.xyz/api/imagegen?type=deepfry&image={url}"
        r = requests.get(b, allow_redirects=True)
        r = r.content.decode('utf8')
        rr = json.loads(r)
        if rr["status"] == 200:
            final = rr["message"]
            if randomizecolor:
                e = discord.Embed(color=discord.Color.random())
            else:
                e = discord.Embed(color=embedcolor)
            e.set_image(url=final)
            await message.channel.send(embed=e)
            await message.delete()
        else:
            await message.channel.send('Oops! something is wrong.', delete_after=2)
            return

    if command == "pingweb" or command == "website":
        b = " ".join(args).replace('https://', "").replace('http://', "")
        param = '-n' if platform.system().lower()=='windows' else '-c'
        command = ['ping', param, '1', b]
        a = subprocess.call(command) == 0
        if a:
            await message.channel.send(f"{b} is up!")
        else:
            await message.channel.send(f"{b} is down!")


bot.run(token, bot=False)
