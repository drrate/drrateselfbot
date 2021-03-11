


#import bullshits
from discord.ext import tasks, commands
import json, time, discord, requests, random, os, asyncio, subprocess, platform, datetime, aiohttp, string


yes = "✅"
no = "❎"


version = '1.1'


#config reading  

burn = ["""
🟥🟥🟥🟥🟥🟥
🟧🟧🟧🟧🟧🟧
🟨🟨🟨🟨🟨🟨
🟩🟩🟩🟩🟩🟩
🟦🟦🟦🟦🟦🟦
🟪🟪🟪🟪🟪🟪
""","""
🟥🟥🟥🟥🟥🔥
🟧🟧🟧🟧🟧🔥
🟨🟨🟨🟨🟨🔥
🟩🟩🟩🟩🟩🔥
🟦🟦🟦🟦🟦🔥
🟪🟪🟪🟪🟪🔥
""","""
🟥🟥🟥🟥🔥🔥
🟧🟧🟧🟧🔥🔥
🟨🟨🟨🟨🔥🔥
🟩🟩🟩🟩🔥🔥
🟦🟦🟦🟦🔥🔥
🟪🟪🟪🟪🔥🔥
""","""
🟥🟥🟥🔥🔥🔥
🟧🟧🟧🔥🔥🔥
🟨🟨🟨🔥🔥🔥
🟩🟩🟩🔥🔥🔥
🟦🟦🟦🔥🔥🔥
🟪🟪🟪🔥🔥🔥
""","""
🟥🟥🔥🔥🔥🔥
🟧🟧🔥🔥🔥🔥
🟨🟨🔥🔥🔥🔥
🟩🟩🔥🔥🔥🔥
🟦🟦🔥🔥🔥🔥
🟪🟪🔥🔥🔥🔥
""","""
🟥🔥🔥🔥🔥🔥
🟧🔥🔥🔥🔥🔥
🟨🔥🔥🔥🔥🔥
🟩🔥🔥🔥🔥🔥
🟦🔥🔥🔥🔥🔥
🟪🔥🔥🔥🔥🔥
""","""
🔥🔥🔥🔥🔥🔥
🔥🔥🔥🔥🔥🔥
🔥🔥🔥🔥🔥🔥
🔥🔥🔥🔥🔥🔥
🔥🔥🔥🔥🔥🔥
🔥🔥🔥🔥🔥🔥
"""]









config = open('config.json', 'r')
config = config.read()
config = json.loads(config) 

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



def embederror(errmessage):
    if randomizecolor:
        e = discord.Embed(color=discord.Color.random(), title=f"{no} {errmessage}")
    else: 
        e = discord.Embed(color=embedcolor, title=f"{no} {errmessage}")
    return e

def embedsuccess(ee):
    if randomizecolor:
        e = discord.Embed(color=discord.Color.random(), title=f"{yes} {ee}")
    else: 
        e = discord.Embed(color=embedcolor, title=f"{yes} {ee}")
    return e


bot = commands.Bot(command_prefix=prefix)
@bot.event
async def on_ready():
    whitelist.append(str(bot.user.id))
    print(" __      __        .__   __              /\\          _________      .__   ________.           __   ")
    print("/  \\    /  \\_____  |  |_/  |_  __________)/ ______  /   _____/ ____ |  |_/ ____\\_ |__   _____/  |_ ")
    print("\\   \\/\\/   /\\__  \\ |  |\\   __\\/ __ \\_  __ \\/  ___/  \\_____  \\_/ __ \\|  |\\   __\\ | __ \\ /  _ \\   __\\")
    print(" \\        /  / __ \\|  |_|  | \\  ___/|  | \\/\\___ \\   /        \\  ___/|  |_|  |   | \\_\\ (  <_> )  |  ")
    print("  \\__/\\  /  (____  /____/__|  \\___  >__|  /____  > /_______  /\\___  >____/__|   |___  /\\____/|__|  ")
    print("       \\/        \\/               \\/           \\/          \\/     \\/                \\/             ")
    r = requests.get('https://raw.githubusercontent.com/ProYT303/walterselfbot/main/ver').content.decode("utf8")
    print(f'Logged in as {bot.user.name}#{bot.user.discriminator}, Version: {version}, Newest : {r}')
    global start_time
    start_time = time.time()
    



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
                e = embederror('Thats not an int!')
                await message.channel.send(embed=e)
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
            await message.channel.send(embed=embederror("Are you just gonna delete all of things and get ratelimited?"))
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
            filee = discord.File(f"./{filename}", filename=filename)
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
                    embedd.set_image(url=url)
                    await message.channel.send(embed=embedd)
        else:
            url = bot.user.avatar_url
            if randomizecolor:
                embedd = discord.Embed(color=discord.Color.random(), description="Walter's Selfbot")
            else:
                embedd = discord.Embed(color=embedcolor, description="Walter's Selfbot")
            embedd.set_author(name=f"{bot.user.name}'s Avatar")
            embedd.set_image(url=url)
            await message.channel.send(embed=embedd) 
            requests.get(url)
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
                await message.channel.send(embed=embederror('Please provide link.'), delete_after=3)
                return
        else:
            await message.channel.send(embed=embederror('Please provide link.'), delete_after=3)
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
                e = discord.Embed(color=discord.Color.random(),description=t[0])
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
            embed = discord.Embed(color=discord.Color.random(), description=f"Prefix: {prefix} | Walter's selfbot - https://github.com/ProYT303/walterselfbot")
        else:
            embed = discord.Embed(color=embedcolor, description=f"Prefix: {prefix} | Walter's selfbot - https://github.com/ProYT303/walterselfbot")
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
        embed.add_field(name="shutdown", value="Title said it all, Shutdowns the bot.", inline=False)
        embed.add_field(name="website", value="Pings to website to see if its down/up", inline=True)
        embed.add_field(name="clyde", value="Beep Boop. ", inline=True)
        embed.add_field(name="deepfry", value=":100::100::100::100::100::rofl::rofl::rofl::rofl: :ok_hand::ok_hand::ok_hand::ok_hand:", inline=True) 
        embed.add_field(name="coinflip", value="Heads or tails, i dont care!", inline=True)
        embed.add_field(name="bobux", value="bobux man is here 😳", inline=True)
        embed.add_field(name="loopnick", value="Changes your nickname every single 0.5 sec", inline=True)
        embed.add_field(name="disableloopnick", value="disables it. simple.", inline=True)
        embed.add_field(name="nitro", value='"generates" a nitro link. mostly isnt valid.', inline=True)
        embed.add_field(name="uptime", value='Title said it all. (again)', inline=True)
        embed.add_field(name="webhook", value='Sends a message to webhook, requires link and message content, split with ","', inline=True)
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
            url = message.attachments[0].url
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

    if command == "clyde":
        cly = f"https://nekobot.xyz/api/imagegen?type=clyde&text={'+'.join(args)}"
        r = requests.get(cly, allow_redirects=True)
        r = r.content.decode('utf8')
        r = json.loads(r)
        d = r["message"]
        print(d)
        r = requests.get(d, allow_redirects=True)
        fname = f"{random.randint(1,500)}-clyde.png"
        open(fname, "wb").write(r.content)
        filee = discord.File(f"./{fname}", filename=fname)
        if randomizecolor:
            embed = discord.Embed(color=discord.Color.random())
        else:
            embed = discord.Embed(color=embedcolor)
        embed.set_image(url=f"attachment://{fname}")
        await message.channel.send(file=filee, embed=embed)
        return os.remove(fname)
    if command == "shutdown":
        await message.channel.send('Shutting down the bot..')
        exit()
        
    if command == "coinflip":
        if randomizecolor:
            e = discord.Embed(color=discord.Color.random(), title="Flipping coin..")
        else:
            e = discord.Embed(color=embedcolor, title="Flipping coin..")
        e = await message.channel.send(embed=e)
        rand = random.randint(1,2)
        await asyncio.sleep(0.5)
        if rand == 1:
            if randomizecolor:
                ee = discord.Embed(color=discord.Color.random(), description="You got tails!")
            else:
                ee = discord.Embed(color=embedcolor, description="You got tails!")
            await e.edit(embed=ee)
        else:
            if randomizecolor:
                ee = discord.Embed(color=discord.Color.random(), description="You got heads!")
            else:
                ee = discord.Embed(color=embedcolor, description="You got heads!")
            await e.edit(embed=ee)
    if command == "uptime":
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        await message.channel.send(text)
    if command == "bobux":
        ee = await message.channel.send('Bobux Generator Is Loading... https://tenor.com/bpeeP.gif')
        await asyncio.sleep(1)
        e = random.randint(1,5)
        switchor = {
            1: "https://cdn.discordapp.com/attachments/808271799153983508/819070121858564116/0bobux.mp4",
            2: "https://cdn.discordapp.com/attachments/808271799153983508/819070307431874560/0bobuxsad.mp4",
            3: "https://cdn.discordapp.com/attachments/804031549477355524/818843084058132500/BOBUX.mp4",
            4: "https://cdn.discordapp.com/attachments/808271799153983508/819071843603972096/1mBOBUXPOG.mp4",
            5: "https://cdn.discordapp.com/attachments/808271799153983508/819071277955284992/rickinfinitbobux.mp4"
        }
        await ee.edit(content=switchor.get(e))
    if command == "webhook":
        async def send(url, msg):
            async with aiohttp.ClientSession() as session:
                try:
                    webhook = discord.Webhook.from_url(url, adapter=discord.AsyncWebhookAdapter(session))
                    await webhook.send(msg, username="Walter's Selfbot", avatar_url=bot.user.avatar_url)
                    await message.channel.send(embed=embedsuccess("Sended"))
                except:
                    await message.channel.send(embed=embederror("Not a valid webhook URL \n `Usage: <webhookurl>, <message>`"))
        
        e = " ".join(args).split(',', 2)
        if len(e) == 2:
            await send(e[0], e[1])
        else:
            await message.channel.send(embed=embederror('`Usage: <webhookurl>, <message>`'))

    if command == "loopnick":
        def spt(word):
            return [char for char in word] 
        e = spt(" ".join(args))
        if message.author.id != bot.user.id:
            return
        global ln

        @tasks.loop(seconds=0.2)
        async def ln(e):
            lol = []
            for i in e:
                print(lol)
                if len(lol) > len(e):
                    lol = []
                lol.append(i)
                await message.author.edit(nick="".join(lol))
        await ln.start(e)
        await message.channel.send(embed=embedsuccess('Started!'))
    if command == "disableloopnick":
        ln.cancel()
        if message.author.id != bot.user.id:
            return
        await message.author.edit(nick="")
        await message.channel.send(embed=embedsuccess('Stopped!'))
    if command == "meme":
        if len(args) == 0:
            await message.channel.send('Usage : ```+meme upper text, bottom text, link```')
        if len(args):
            joined = " ".join(args)
            splitted = joined.split(",")
            if len(splitted) < 3:
                await message.channel.send('Usage : ```+meme upper text, bottom text, link``` TIP : use space to fill blank')
            else:
                uppertext = splitted[0]
                bottomtext = splitted[1]
                links = splitted[2]
                uppertext = uppertext.replace("-", "_").replace(' ', "%20")
                bottomtext = bottomtext.replace("-", "_").replace(' ', "%20")
                links = links.replace(" ", "")
                
                a = f"https://api.memegen.link/images/custom/{uppertext}/{bottomtext}.png?background={links}"
                print(f"Downloading {a}")            
                r = requests.get(a, allow_redirects=True)
                filename = f"meme-${random.randint(1, 500)}.png"
                open(filename, 'wb').write(r.content)
                await message.channel.send(file=discord.File(filename))
                os.remove(filename)
    if command == "join":
        
        invcode = args[0].replace('https://', "").replace('http://', "").replace('discord.gg/', "").replace('discord.com/invite/', "")
        r = requests.post(f"https://discord.com/api/v8/invites/{invcode}",headers={'authorization':token})
        if r.Response == 200:
            await message.channel.send(embed=embederror(f"{yes} Joined!"))
        else:
            await message.channel.send(embed=embederror("Join command failed successfully."))
    if command == "nick":
        if message.mentions:
            user = message.mentions[0]
            args.pop(0)
        elif args:
            try:
                user = bot.get_user(args[0])
                args.pop(0)
            except:
                await message.channel.send(embed=embederror('Seemed like its not a userid.'))
        
        if user:
            await user.edit(nick=" ".join(args))
        else:
            await message.channel.send(embed=embederror(' Usage: ```nick mention/userid <new name>```'))
    if command == "purgeall":
        if args:
            try:
                limit = int(args[0])
            except:
                await message.channel.send(embed=embederror("Thats not an int!"))
                return
            await message.delete()
        else:
            await message.channel.send(embed=embederror("Are you just gonna delete all of things and get ratelimited?"))
        e = []
        async for m in message.channel.history():
                if len(e) == limit:
                    break
                else:
                    e.append('E')
                    try:
                        await m.delete()
                    except:
                        print('No permission.')
                        break
    if command == "nitro":
        if args:
            try:
                limit = int(args[0])
                print('ok, generating')
            except:
                print('ok, generating')
                limit = 5
        for i in range(limit):
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            await message.channel.send(f"discord.gift/{code}")
            await asyncio.sleep(0.2)
    if command == "version":
        r = requests.get('https://raw.githubusercontent.com/ProYT303/walterselfbot/main/ver')
        await message.channel.send(f"""Version: {version}
Newest version : {r.content.decode('utf8')}""")
    if command == "gayburn":
        a = None
        a = await message.channel.send("Burning gay flag..")
    for i in burn:
        await a.edit(content=i)
        await asyncio.sleep(1)

bot.run(token, bot=False) 


