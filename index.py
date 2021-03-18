try:
    from discord.ext import tasks, commands
    import json, time, discord, requests, random, os, asyncio, subprocess, platform, datetime, aiohttp, string, math
except:
    print('Required libs isnt installed, installing..')
    import os
    if os.name == "nt":
        # windows
        os.system("py -3 -m pip install requests discord.py")
    else:
        # linux, mac, bsd, openbsd, etc
        os.system("python3 -m pip install requests discord.py")
    print("Installed!")
    print('Importing libs..')
    from discord.ext import tasks, commands
    import json, time, discord, requests, random, os, asyncio, subprocess, platform, datetime, aiohttp, string, math
    print ("Done!")
yes = "✅"
no = "❎"


versione = '2.4'


#config reading  

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
try:
    config = open('config.json', 'r')
    config = config.read()

    config = json.loads(config) 
except:
    print("config.json isnt in the folder, terminating ( for help, go https://discord.gg/kuSzstZyFf or https://discord.io/walters )")
    time.sleep(5)
    exit()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

prefix = config["prefix"]
token = config["token"]
embedcolor = config["embedcolor"]
firstsnipe = config["firstsnipe"]

if config["randomcolor"] == "true": 
    randomizecolor = True
else: 
    randomizecolor = False 
    embedcolor = getcolor(embedcolor)

if firstsnipe.lower() == 'true':
    global frr
    frr = True



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

intents = discord.Intents().all()

bot = commands.Bot(prefix, self_bot=True, case_insensitive=True, intents=intents)
bot.remove_command('help')
@bot.event
async def on_ready():
    print(bcolors.OKGREEN)
    print(" __      __        .__   __              /\\          _________      .__   ________.           __   ")
    print("/  \\    /  \\_____  |  |_/  |_  __________)/ ______  /   _____/ ____ |  |_/ ____\\_ |__   _____/  |_ ")
    print("\\   \\/\\/   /\\__  \\ |  |\\   __\\/ __ \\_  __ \\/  ___/  \\_____  \\_/ __ \\|  |\\   __\\ | __ \\ /  _ \\   __\\")
    print(" \\        /  / __ \\|  |_|  | \\  ___/|  | \\/\\___ \\   /        \\  ___/|  |_|  |   | \\_\\ (  <_> )  |  ")
    print("  \\__/\\  /  (____  /____/__|  \\___  >__|  /____  > /_______  /\\___  >____/__|   |___  /\\____/|__|  ")
    print("       \\/        \\/               \\/           \\/          \\/     \\/                \\/             ")
    print(bcolors.ENDC)
    r = requests.get('https://raw.githubusercontent.com/ProYT303/walterselfbot/main/ver').content.decode("utf8")

    print(f'{bcolors.OKBLUE}Logged in as {bot.user.name}#{bot.user.discriminator}{bcolors.ENDC}, {bcolors.OKGREEN}Version: {versione}, Newest : {r}{bcolors.ENDC}')
    global start_time
    start_time = time.time()



@bot.event
async def on_guild_channel_create(channel):
    try:
        if frr:
            if "ticket" in channel.name: return
            try:
                await channel.send('first')
                print(f'first on {channel.name} in {channel.guild}')
            except:
                print(f'No access on {channel.guild} - {channel.name}')
    except:
        int("2") # ok
        

@bot.command()
async def help(ctx):
    
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)

    if randomizecolor:
        embed = discord.Embed(color=discord.Color.random(), description=f"Prefix: {prefix} | Walter's selfbot - https://github.com/ProYT303/walterselfbot | Tehc Suport : https://discord.gg/kuSzstZyFf")
    else:
        embed = discord.Embed(color=embedcolor, description=f"Prefix: {prefix} | Walter's selfbot - https://github.com/ProYT303/walterselfbot | Tehc Suport : https://discord.gg/kuSzstZyFf")
    embed.add_field(name="utilities", value="ping,spam,imageembed,embed,avatar,nitro,webhook,playing,watching,listening,streaming,statusclear,ghostping,dmspam,dmall,loopstatus,disableloopstatus,loopnick,status_sync,disablestatus_sync", inline=False)
    embed.add_field(name="media", value="trump,recaptcha,clyde,deepfry,bobux,dog,minecraft,corona,proxy,meme", inline=True)
    embed.add_field(name="etc", value="shutdown,website,coinflip,uptime,loopnick,disableloopnick,predictgender,lag,bitcoin,pi", inline=True)
    embed.add_field(name="moderation", value=r'purge,purgeall,nick', inline=True)
    embed.add_field(name="dogecoin", value=r'dogetotal,dogebal,dogediff ', inline=True)
 # help command        
#
#
#
 #
#
#
#
#
#
 #       
    await ctx.send(embed=embed)  

@bot.command( aliases=['ghostspam'])
async def ghostping(ctx, *args):
    
    args = list(args)
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    limit = int(args[0])
    args.pop(0)
    msg = " ".join(args)
    for i in range(limit):
        await ctx.send(msg, delete_after=0.3)
        await asyncio.sleep(0.4)

@bot.command()
async def proxy(ctx):
    
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    if os.path.exists('proxy.txt') == False:
        file = open("proxy.txt", "a+")
        res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
        proxies = []
        for proxy in res.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            file.write((p)+"\n")
        file = open("proxy.txt", "a+")
        res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
        proxies = []
        for proxy in res.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            file.write((p)+"\n")
    if os.path.exists('socks4proxy.txt') == False:
        file = open("socks4proxy.txt", "a+")
        res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
        proxies = []
        for proxy in res.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            file.write((p)+"\n")
    if os.path.exists('socks5proxy.txt') == False:
        file = open("socks5proxy.txt", "a+")
        res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
        proxies = []
        for proxy in res.text.split('\n'):
            proxy = proxy.strip()
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            file.write((p)+"\n")
    await ctx.send(file=discord.File('proxy.txt'))
    await ctx.send(file=discord.File('socks5proxy.txt'))
    await ctx.send(file=discord.File('socks4proxy.txt'))
@bot.command( aliases=['listening'])
async def listen(ctx, *args):
    
    args = list(args)
    spl = " ".join(args) 
    if spl:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=spl))
        await ctx.send(embed=embedsuccess('Success!'))
    else:
        await ctx.send(embed=embederror("What ya gonna listen to"))
@bot.command( aliases=['play'])
async def playing(ctx, *args):
    
    args = list(args)
    if args: 
        try: 
            await bot.change_presence(activity=discord.Game(name=" ".join(args)))
            await ctx.send(embed=embedsuccess('Successfully changed status!'))
        except:
            await ctx.send(embed=embederror('Failed!'))
    else:
        await ctx.send(embed=embederror("What ya gonna play tho"))

@bot.command( aliases=['clearlistening', 'statusclear'])
async def clearstatus(ctx, *args):
    
    args = list(args) 
    try:
        await bot.change_presence(activity=discord.Game(name=""))
        await ctx.send(embed=embedsuccess('Successfully cleared status!'))
    except:
        await ctx.send(embed=embederror('Failed!'))

@bot.command( aliases=['watching'])
async def watch(ctx, *args):   
    
    args = list(args)  
    if args:
        try:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" ".join(args)))
            await ctx.send(embed=embedsuccess('Successfully changed status!'))
        except:
            await ctx.send(embed=embederror('Failed!'))
    else:
        await ctx.send(embed=embederror("What ya gonna watch to"))

@bot.command( aliases=['ver'])
async def version(ctx, *args):    
    
    r = requests.get('https://raw.githubusercontent.com/ProYT303/walterselfbot/main/ver')
    await ctx.send(f"""Version: {versione}
Newest version : {r.content.decode('utf8')}""")

@bot.command( aliases=['nitrogen'])
async def nitro(ctx, *args):   
    
    args = list(args) 
    if args:
        try:
            limit = int(args[0])
            print('ok, generating')
        except:
            print('ok, generating')
            limit = 5
    else:
        limit = 5
    for i in range(limit):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.send(f"discord.gift/{code}")
        await asyncio.sleep(0.2)
@bot.command( aliases=['supportserver', 'support', 'techsupport'])
async def server(ctx, *args): 
    
    invcode = "kuSzstZyFf"
    r = requests.post(f"https://discord.com/api/v8/invites/{invcode}",headers={'authorization':token})
    print(r)
    if r.content:
        await ctx.send(embed=embedsuccess(f"Joined Support Server!"))
    else:
        await ctx.send(embed=embederror("failed successfully."))
@bot.command( aliases=['hax'])
async def hack(ctx, *args): 
    
    args = list(args) 
    if args:
        hac = " ".join(args)
    else:
        return await ctx.send(embed=embederror('Are you trying to hack yourself?'))
    msg = await ctx.send(f'Hacking {hac}.')
    e = []
    for i in range(2):
        e.append('.')
        await msg.edit(content=f'Hacking {hac}.{"".join(e)}')
        await asyncio.sleep(0.1)
    await msg.edit(content='Bypassing windows antihack...')
    await asyncio.sleep(2)
    await msg.edit(content='Getting user-token..')
    await asyncio.sleep(2)
    await msg.edit(content='Reporting to FBI...')
    await asyncio.sleep(2)
    await msg.edit(content=f'Successfully hacked {hac}')
@bot.command( aliases=['purgemod'])
async def purgeall(ctx, *args): 
    
    if args:
        try:
            limit = int(args[0])
        except:
            await ctx.send(embed=embederror("Thats not an int!"))
            return
        try:
            await ctx.message.delete()
        except:
            print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    else:
        await ctx.send(embed=embederror("Are you just gonna delete all of things and get ratelimited? give me limit."))
    e = []
    async for m in ctx.channel.history():
            if len(e) == limit:
                break
            else:
                e.append('E')
                try:
                    await m.delete()
                except:
                    print('No permission.')
                    break
@bot.command( aliases=['nickmod'])
async def nick(ctx, user: discord.Member = None, *args ):    
      
    if user:
        await user.edit(nick=" ".join(args))
        await ctx.send(embed=embedsuccess('Successfully changed nickname!'))
    else:
        await ctx.send(embed=embederror(' Usage: ```nick mention/userid <new name>```'))

@bot.command( aliases=['joinserver'])
async def join(ctx, *args ):      
    
    invcode = args[0].replace('https://', "").replace('http://', "").replace('discord.gg/', "").replace('discord.com/invite/', "")
    r = requests.post(f"https://discord.com/api/v8/invites/{invcode}",headers={'authorization':token})
    if r == 200:
        await ctx.send(embed=embederror(f"Joined!"))
    else:
        await ctx.send(embed=embederror("Join command failed successfully."))
@bot.command( aliases=['memegen'])
async def meme(ctx, *args):      
    
    args = list(args)
    if len(args) == 0:
        await ctx.send('Usage : ```+meme upper text, bottom text, link```')
    if len(args):
        joined = " ".join(args)
        splitted = joined.split(",")
        if len(splitted) < 3:
            await ctx.send('Usage : ```+meme upper text, bottom text, link``` TIP : use space to fill blank')
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
            await ctx.send(file=discord.File(filename))
            os.remove(filename)
@bot.command( aliases=['cyclenick', 'nickloop'])
async def loopnick(ctx, *args):     
     
    args = list(args)
    def spt(word):
        return [char for char in word] 
    e = spt(" ".join(args))
    if ctx.author.id != bot.user.id:
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
            await ctx.author.edit(nick="".join(lol))
    await ln.start(e)
    await ctx.send(embed=embedsuccess('Started!'))
@bot.command( aliases=['disablecyclenick', 'disablecyclenicknickloop'])
async def disableloopnick(ctx, *args): 
         
    ln.cancel()
    if ctx.author.id != bot.user.id:
        return
    await ctx.author.edit(nick="")
    await ctx.send(embed=embedsuccess('Stopped!'))
@bot.command( aliases=['webhooksend', 'sendwebhook'])
async def webhook(ctx, *args):      
    
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    args = list(args)
    async def send(url, msg):
        async with aiohttp.ClientSession() as session:
            try:
                webhook = discord.Webhook.from_url(url, adapter=discord.AsyncWebhookAdapter(session))
                await webhook.send(msg, username="Walter's Selfbot", avatar_url=bot.user.avatar_url)
                await ctx.send(embed=embedsuccess("Sended"))
            except:
                await ctx.send(embed=embederror("Not a valid webhook URL \n `Usage: <webhookurl>, <message>`"))
    
    e = " ".join(args).split(',', 2)
    if len(e) == 2:
        await send(e[0], e[1])
    else:
        await ctx.send(embed=embederror('`Usage: <webhookurl>, <message>`'))
@bot.command( aliases=['bobux', 'bobuxgenerator'])
async def robux(ctx, *args):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    
    ee = await ctx.send('Bobux Generator Is Loading... https://tenor.com/bpeeP.gif')
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
@bot.command(case_insensitive=True)
async def uptime(ctx, *args):    
    
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    await ctx.send(text)
@bot.command(case_insensitive=True)
async def coinflip(ctx, *args):  
    
    if randomizecolor:
        e = discord.Embed(color=discord.Color.random(), title="Flipping coin..")
    else:
        e = discord.Embed(color=embedcolor, title="Flipping coin..")
    e = await ctx.send(embed=e)
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
@bot.command(case_insensitive=True)
async def shutdown(ctx):
    
    await ctx.send('Shutting down the bot..')
    exit()
@bot.command(case_insensitive=True)
async def clyde(ctx, *args):  
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    
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
    await ctx.send(file=filee, embed=embed)
@bot.command(case_insensitive=True)
async def website(ctx, *args):  
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    
    b = " ".join(args).replace('https://', "").replace('http://', "")
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', b]
    a = subprocess.call(command) == 0
    if a:
        await ctx.send(f"{b} is up!")
    else:
        await ctx.send(f"{b} is down!")

@bot.command(case_insensitive=True)
async def deepfry(ctx, user:discord.Member=None,*args): 
    
    if user:
        url = user.avatar_url
    else:
        if args:
            url=args[0]
        else:
            await ctx.send(embed=embederror('Please put link/mentions'), delete_after=3)
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
        await ctx.send(embed=e)
        try:
            await ctx.message.delete()
        except:
            print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    else:
        await ctx.send('Oops! something is wrong.', delete_after=2)
        return


@bot.command(case_insensitive=True)
async def ascii(ctx, *args):
    
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    a = "+".join(args)
    b = f"https://artii.herokuapp.com/make?text={a}"
    r = requests.get(b, allow_redirects=True)
    asci = f"```{r.content.decode('utf8')}```"
    if len(a) < 11:
        if randomizecolor:
            e = discord.Embed(color=discord.Color.random()) 
        else:
            e = discord.Embed(color=embedcolor)
        e.add_field(name="Ascii Generated!", value=asci, inline=False)
        await ctx.send(embed=e)
    else:
        await ctx.send(asci)
@bot.command(case_insensitive=True)
async def embed(ctx, *args):   
    
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    t = " ".join(args).split(",")
    if len(t) == 1:
        if randomizecolor:
            e = discord.Embed(color=discord.Color.random(),description=t[0])
        else:
            e = discord.Embed(color=embedcolor,description=t[0])
        
        await ctx.send(embed=e)
    elif len(t) == 2 or len(t) > 2:
        if randomizecolor:
            e = discord.Embed(color=discord.Color.random(), title=t[0], description=t[1])
        else:
            e = discord.Embed(color=embedcolor, title=t[0], description=t[1])
        
        await ctx.send(embed=e)
@bot.command(case_insensitive=True)
async def imageembed(ctx, *args):
    
    args = list(args)
    if args:
        if args[0].startswith('https://') or args[0].startswith('http://'):
            url = args[0]
        else:
            await ctx.send(embed=embederror('Please provide link.'), delete_after=3)
            return
    else:
        await ctx.send(embed=embederror('Please provide link.'), delete_after=3)
        return
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    
    if randomizecolor:
        embedd = discord.Embed(color=discord.Color.random(), description="Walter's Selfbot")
    else:
        embedd = discord.Embed(color=embedcolor, description="Walter's Selfbot")
    embedd.set_image(url=url)    
    await ctx.send(embed=embedd)
@bot.command(case_insensitive=True)
async def spam(ctx, *args):
    
    args = list(args)
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    limit = int(args[0])
    args.pop(0)
    msg = " ".join(args)
    for i in range(limit + 1):
        await ctx.send(msg)
        await asyncio.sleep(0.4)
@bot.command( aliases=["captcha", 'rcaptcha', 'googlecaptcha'])
async def recaptcha(ctx, *args):
    
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
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
        await ctx.send(file=filee, embed=embedd)
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
        await ctx.send(file=filee, embed=embedd)
        os.remove(filename)
@bot.command(case_insensitive=True)
async def purge(ctx, *args):
    
    args = list(args)
    if args:
        try:
            limit = int(args[0])
        except:
            e = embederror('Thats not an int!')
            await ctx.send(embed=e)
        try:
            await ctx.message.delete()
        except:
            print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
        mymessages = []
        async for m in ctx.channel.history():
            if len(mymessages) == limit:
                break
            if m.author == bot.user:
                mymessages.append('deleted some')
                try:
                    await m.delete()
                except:
                    print('error :flushed:') 
@bot.command(case_insensitive=True)
async def trump(ctx, *args):
    
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    if len(args):
        trumpo = f"https://api.no-api-key.com/api/v2/trump?message={'%20'.join(args)}"
        r = requests.get(trumpo, allow_redirects=True)
        filename = f"trump-${random.randint(1, 500)}.png"
        open(filename, 'wb').write(r.content)
        await ctx.send(file=discord.File(filename))
        os.remove(filename)
    else:
        trumpo = f"https://api.no-api-key.com/api/v2/trump?message=ok%20what%20should%20i%20say"
        r = requests.get(trumpo, allow_redirects=True)
        filename = f"noargs-trump-${random.randint(1, 500)}.png"
        open(filename, 'wb').write(r.content)
        await ctx.send(file=discord.File(filename))
        os.remove(filename)  

@bot.command(case_insensitive=True)
async def ping(ctx, *args):
    
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    print('e')
    before = time.monotonic()
    if randomizecolor:
        embedd = discord.Embed(title="Pinging..",color=discord.Color.random(), description="Walter's Selfbot")
    else:
        embedd = discord.Embed(title="Pinging..",color=embedcolor, description="Walter's Selfbot")
    message = await ctx.send(embed=embedd)
    ping = (time.monotonic() - before) * 1000
    if randomizecolor:
        embeddd = discord.Embed(title=f"Pong! {int(ping)}ms",color=discord.Color.random(), description="Walter's Selfbot")
    else:
        embeddd = discord.Embed(title=f"Pong! {int(ping)}ms",color=embedcolor, description="Walter's Selfbot")
    
    await message.edit(embed=embeddd)
    print(f'Ping {int(ping)}ms')
@bot.command(case_insensitive=True)
async def avatar(ctx, user: discord.Member = None):
    
    if user:
        url = user.avatar_url
    if url:
        if randomizecolor:
            embedd = discord.Embed(color=discord.Color.random(), description="Walter's Selfbot")
        else:
            embedd = discord.Embed(color=embedcolor, description="Walter's Selfbot")
        embedd.set_author(name=f"{user.name}'s Avatar")
        embedd.set_image(url=url)
        await ctx.send(embed=embedd)
@bot.command(case_insensitive=True, aliases=['getrandomnum', 'randomnumber', 'random'])
async def getrandom(ctx, *args):
    
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    if args:
        args = " ".join(args)
        args = args.split('|')
        if len(args) == 1:
            return await ctx.send(embed=embederror('Usage: `min | max`')) 

        if len(args) == 2:
            try:
                minim = int(args[0])
                maxim = int(args[1])
            except:
                return await ctx.send('Thats not even a number smh')
            a = await ctx.send('Prepare for randomness')
            await asyncio.sleep(1)
            for i in range(10):
                await a.edit(content=str(random.randint(minim, maxim)))
                await asyncio.sleep(1)
        else:
            minim = 1
            maxim = random.randint(500, 1500)
            a = await ctx.send('Prepare for randomness')
            await asyncio.sleep(1)
            for i in range(10):
                await a.edit(content=str(random.randint(minim, maxim)))
                await asyncio.sleep(1)
    else:
        minim = 1
        maxim = random.randint(500, 1500)
        a = await ctx.send('Prepare for randomness')
        await asyncio.sleep(1)
        for i in range(10):
            await a.edit(content=str(random.randint(minim, maxim)))
            await asyncio.sleep(1)
@bot.command(aliases=['tableflip'])
async def fliptable(ctx):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    await ctx.message.delete()
    a = await ctx.send('┬─┬ ノ( ゜-゜ノ)')
    await asyncio.sleep(0.5)
    await a.edit(content='(╯°□°）╯︵ ┻━┻')
@bot.command(aliases=['dmspam'])
async def spamdm(ctx, member: discord.Member = None, *args):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    if args:
        args = list(args)
        if member:
            try:
                limit = int(args[0])
                args.pop(0)
            except:
                return await ctx.send(embed=embederror('Isnt even number. Usage : `member limit(int) message`'))

            msg = " ".join(args)
            if msg:
                await ctx.send(embed=embedsuccess(f"Spamming {member}'s dms!"))
                for i in range(limit):
                    await member.send(msg)
                    await asyncio.sleep(1)
            else:
                return await ctx.send('What the fuck was should be the message? specify it. ')
@bot.command(aliases=['streaming'])
async def stream(ctx,*args):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    if args:
        await bot.change_presence(activity=discord.Streaming(name=" ".join(args), url='https://www.youtube.com/watch?v=iik25wqIuFo&feature=emb_title'))
        await ctx.send(embed=embedsuccess('Successfully changed status!'))
    else:
        await ctx.send(embed='What should ya stream?')
@bot.command(aliases=['dogecoinbalance', 'dogecoinbal'])
async def dogebal(ctx,*args):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    args = list(args)
    print(args)
    if args:
        link = f"http://dogechain.info/chain/Dogecoin/q/addressbalance/{args[0]}"

        r = requests.get(link, allow_redirects=True)
        r = r.content.decode('utf8')
        if randomizecolor:
            e = discord.Embed(color=discord.Color.random(), title=f"{args[0]}'s Balance", description=f"{r} DOGES")
        else: 
            e = discord.Embed(color=embedcolor, title=f"{args[0]}'s Balance", description=f"{r} DOGES")   
        await ctx.send(embed=e)
    else:
        await ctx.send(embed=embederror('What was the dogecoin address?'), delete_after=3)
@bot.command(aliases=['dogecoindifficulty', 'dogedifficulty'])
async def dogediff(ctx):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    link = f"http://dogechain.info/chain/Dogecoin/q/getdifficulty"

    r = requests.get(link, allow_redirects=True)
    r = r.content.decode('utf8')
    if randomizecolor:
        e = discord.Embed(color=discord.Color.random(), title=f"Last solved block's difficulty : {r}")
    else: 
        e = discord.Embed(color=embedcolor, title=f"Last solved block's difficulty : {r}")
    await ctx.send(embed=e)
@bot.command(aliases=['dogecointotal', 'dogestotal'])
async def dogetotal(ctx):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    link = f"https://dogechain.info/chain/Dogecoin/q/totalbc"

    r = requests.get(link, allow_redirects=True)
    r = r.content.decode('utf8')
    if randomizecolor:
        e = discord.Embed(color=discord.Color.random(), title=f"Dogecoin mined total : {r}")
    else: 
        e = discord.Embed(color=embedcolor, title=f"Dogecoin mined total : {r}")
    await ctx.send(embed=e)
@bot.command(aliases=['covid19', 'covid'])
async def corona(ctx):     
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    r = requests.get('https://covid19.mathdro.id/api', allow_redirects=True)
    r = json.loads(r.content.decode('utf8'))
    n = r["confirmed"]      
    n = n["value"]
    millnames = ['',' Thousand',' Million',' Billion',' Trillion']
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    Case = '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])
    n = r["recovered"]
    n = n["value"]
    millnames = ['',' Thousand',' Million',' Billion',' Trillion']
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    Recovered = '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

    n = r["deaths"]
    n = n["value"]
    millnames = ['',' Thousand',' Million',' Billion',' Trillion']
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    Deaths = '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])
    if randomizecolor:
        e = discord.Embed(color=discord.Color.random(), title='Covid-19 Information', description="Walter's Selfbot | stay @ home pls")
    else:
        e = discord.Embed(color=embedcolor, title='Covid-19 Information', description="Walter's Selfbot | stay @ home pls")
    e.add_field(name="Confirmed cases", value=Case)
    e.add_field(name="Recovered", value=Recovered)
    e.add_field(name="Deaths", value=Deaths)
    await ctx.send(embed=e)
@bot.command(aliases=['countryip', 'iptocountry'])
async def ipcountry(ctx, *args):     
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    args = list(args)
    if args:
        
        link = f"https://api.ip2country.info/ip?{args[0]}"
        r = requests.get(link, allow_redirects=True)
        r = json.loads(r.content.decode('utf8'))
        await ctx.send(embed=embedsuccess(f'{args[0]} is in {r["countryName"]}'))
    else:
        await ctx.send(embed=embederror('What was the ip? specify it.'))
        
@bot.command(aliases=['unixtime', 'unixtimestamp'])
async def unix(ctx, *args):     
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    args = list(args)
    if args:
        link = f"https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp={args[0]}"
        r = requests.get(link, allow_redirects=True)
        
        r = r.content.decode('utf8')
        if r == '{"Error":"Input string was not in a correct format."}':
            return await ctx.send(embed=embederror('Invalid unixtimestamp/timestamp isnt supplied'))    
        await ctx.send(f"{args[0]} => {r}")
    else:
        await ctx.send(embed=embederror('Invalid unixtimestamp/timestamp isnt supplied'))
@bot.command(aliases=['predictgender', 'gender'])
async def gendername(ctx, *args):   
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)  
    if args:
        link = f"https://api.genderize.io?name={' '.join(args).replace(' ', '')}"
        r = requests.get(link, allow_redirects=True)
        r = json.loads(r.content.decode('utf8'))
        gender = r["gender"]
        name = r["name"]
        probability = r["probability"]
        probability = f"{probability * 100}%"
        if randomizecolor:
            e = discord.Embed(color=discord.Color.random(), description="Walter's selfbot", title=f"{name}'s Predicted gender")
        else:
            e = discord.Embed(color=discord.Color.random(), description="Walter's selfbot", title=f"{name}'s Predicted gender")
        e.add_field(name="Gender", value=gender)
        e.add_field(name="Probability", value=probability)
        await ctx.send(embed=e)
    else:
        return await ctx.send(embed=embederror('Name isnt supplied'))
@bot.command(aliases=['dogs'])
async def dog(ctx, *args):     
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    r = requests.get("https://dog.ceo/api/breeds/image/random", allow_redirects=True)
    r = json.loads(r.content.decode('utf8'))
    if r["status"] == "success":
        await ctx.send(r["message"])
    else:
        await ctx.send(embed=embederror('Failed.'))
@bot.command(aliases=['achievement'])
async def minecraft(ctx, *args):  
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    if args:
        r = requests.get(f"https://minecraftskinstealer.com/achievement/{random.randint(1,30)}/Achievement+Get%21/{'+'.join(args)}", allow_redirects=True)
        r = r.content
        f = f"{random.randint(1,203)}-achievement-walterselfbot.png"
        open(f, "wb").write(r)
        await ctx.send(file=discord.File(f"./{f}"))
        os.remove(f)
    else:
        await ctx.send(embed=embederror('achievement : nothing'))

@bot.command()
async def bitcoin(ctx):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    resp = requests.get('https://blockchain.info/ticker')
    pret = resp.json()['USD']['last']
    pret1 = resp.json()['EUR']['last']
    pret2 = resp.json()['GBP']['last']
    try:
        if randomizecolor:
            embed = discord.Embed(color=discord.Color.random(), title="Bitcoin Price")
        else:
            embed = discord.Embed(color=embedcolor, title="Bitcoin Price")
        embed.add_field(name="BTC Current Price:", value=f"${pret}\n€{pret1}\n£{pret2}", inline=True)
        embed.set_thumbnail(url="https://st3.depositphotos.com/5906102/14454/v/600/depositphotos_144548047-stock-illustration-crypto-currency-bitcoin-golden-symbol.jpg")
        await ctx.send(embed=embed)
    except:
        ctx.send("BTC Current Price:", value=f"${pret}\n€{pret1}\n£{pret2}")
@bot.command(aliases=["lagcord"])
async def lag(ctx, *args):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    if args:
        args = list(args)
        if args[0] == "stop":
            try:
                xdxd.stop()
                return await ctx.send(embed=embedsuccess('Successfully stopped'))
            except:
                return await ctx.send(embed=embederror("Failed stopping lag machien rip"))
        try:
            limit = int(args[0])
        except:
            limit = 5
        msg = []
        for r in ctx.guild.roles:
            msg.append(f"<@&{r.id}>")
        for channel in ctx.guild.channels:
            msg.append(f"<#{channel.id}>")
        if len(msg)*5 < 2001:
            a = "".join(msg), "".join(msg), "".join(msg), "".join(msg), "".join(msg)
        else:
            a = "".join(msg)
        
        @tasks.loop(seconds=1,count=limit)
        async def xdxd():
            await ctx.send(" ".join(a))
        xdxd.start()
    else:
        msg = []
        for r in ctx.guild.roles:
            msg.append(f"<@&{r.id}>")
        for channel in ctx.guild.channels:
            msg.append(f"<#{channel.id}>")
        if len(msg)*5 < 2001:
            a = "".join(msg), "".join(msg), "".join(msg), "".join(msg), "".join(msg)
        else:
            a = "".join(msg)
        await ctx.send(" ".join(a))



@bot.command(aliases=['dm_all', "directmessageall","directmessage_all"])
async def dmall(ctx, *args):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    args = list(args)
    if args:
        members = ctx.guild.members
        for member in members:
            if member == bot.user:
                break
            try:
                if len(" ".join(args)) > 2000: 
                  return await ctx.send(embed=embederror("Discord Limit / Message cant be 2000>"))
                await member.send(" ".join(args))
                print(f"{bcolors.OKGREEN}[DMALL] Successfully dmed {member.name} with {' '.join(args)}!{bcolors.ENDC}")
            except:
                print(f"{bcolors.FAIL}[DMALL] Failed to dm {member.name}{bcolors.ENDC}")
    else:
        await ctx.send(embed=embederror("A message was not provided."))
@bot.command(aliases=['loop_status'])
async def loopstatus(ctx, *args):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    if args:
        def spt(word):
            return [char for char in word] 
        status = " ".join(args)
        status = spt(status)
        a = True
        global ls
        @tasks.loop(seconds=2)
        async def ls(status):
            xd = []
            for i in status:
                if "".join(xd) == "".join(status):
                    xd = []
                if i == " ":
                    xd.append(i)
                else:
                    xd.append(i)
                    payload = {"custom_status":{"text":"".join(xd)}}
                    e = requests.patch('https://discord.com/api/v8/users/@me/settings', headers={'authorization':token}, json=payload)
                    await asyncio.sleep(1)
        ls.start(status)
        await ctx.send(embed=embedsuccess("Started! this feature is in beta™️"))
    else:
        await ctx.send(embed=embederror('A status was not provided.'))
@bot.command(aliases=['disableloop_status'])
async def disableloopstatus(ctx, *args):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    try:
        ls.stop()
    except:
        return await ctx.send(embed=embederror("Failed."))
    payload = {"custom_status":{"text":""}}
    e = requests.patch('https://discord.com/api/v8/users/@me/settings', headers={'authorization':token}, json=payload)
    await ctx.send(embed=embedsuccess('Stopped loopstatus!'))
    
@bot.command(aliases=['statussync', 'status_sync'])
async def sync_status(ctx, *args):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    if args:
        def spt(word):
            return [char for char in word] 
        status = " ".join(args)
        if "|" not in status:
            return await ctx.send(embed=embederror("2rd status was not provided, split with | "))
        s = status.split('|')
        global lsb
        @tasks.loop(seconds=len(s))
        async def lsb(status):
            for i in status:
                payload = {"custom_status":{"text":i}}
                e = requests.patch('https://discord.com/api/v8/users/@me/settings', headers={'authorization':token}, json=payload)
                await asyncio.sleep(2)
        lsb.start(s)
        await ctx.send(embed=embedsuccess("Started! this feature is in beta™️"))
    else:
        await ctx.send(embed=embederror('A status was not provided.'))
@bot.command(aliases=['disablestatus_sync'])
async def disablestatussync(ctx, *args):
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    lsb.stop()
    payload = {"custom_status":{"text":""}}
    e = requests.patch('https://discord.com/api/v8/users/@me/settings', headers={'authorization':token}, json=payload)
    await ctx.send(embed=embedsuccess('Stopped status sync!'))
@bot.command(aliases=['generatepi'])
async def pi(ctx, *args):
    if args: d = args[0]
    else: 
        await ctx.send(embed=embederror("Limit was not provided, continuing with 100"))
        d = 100
    
    def pi_digits(x):
        x = int(x)
        k,a,b,a1,b1 = 2,4,1,12,4
        while x > 0:
            p,q,k = k * k, 2 * k + 1, k + 1
            a,b,a1,b1 = a1, b1, p*a + q*a1, p*b + q*b1
            d,d1 = a/b, a1/b1
            while d == d1 and x > 0:
                yield int(d)
                x -= 1
                a,a1 = 10*(a % b), 10*(a1 % b1)
                d,d1 = a/b, a1/b1
    try:
        d = int(d) + 3
        if d > 1900:
            return await ctx.send(embed=embederror('Cant be greater than 1900'))
    except:
        await ctx.send(embed=embederror('Input was not an int'))
        exit()
    digits = [str(n) for n in list(pi_digits(d))]
    digits = digits[:1] + ['.'] + digits[1:]
    if randomizecolor:
        r = discord.Embed(color=discord.Color.random(), description=f"Generated with spigot's algorithm ```\n{''.join(digits)}\n```")
    else:
        r = discord.Embed(color=embedcolor,description=f"Generated with spigot's algorithm ```\n{''.join(digits)}\n```")
    await ctx.send(embed=r)
bot.run(token, bot=False)
