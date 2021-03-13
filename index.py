from discord.ext import tasks, commands
import json, time, discord, requests, random, os, asyncio, subprocess, platform, datetime, aiohttp, string
yes = "✅"
no = "❎"


versione = '2.2'


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
config = open('config.json', 'r')
config = config.read()
config = json.loads(config) 

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
whitelist = config["whitelisted"]       
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


bot = commands.Bot(prefix, self_bot=True, case_insensitive=True)
bot.remove_command('help')
@bot.event
async def on_ready():
    whitelist.append(str(bot.user.id))
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
    print(whitelist)
    global start_time
    start_time = time.time()


def checkw(ide):
    ide = str(ide)
    if ide not in whitelist:
        return

@bot.event
async def on_guild_channel_create(channel):

    if frr:
        if "ticket" in channel.name: return
        try:
            await channel.send('first')
            print(f'first on {channel.name} in {channel.guild}')
        except:
            print(f'No access on {channel.guild} - {channel.name}')
        

@bot.command()
async def help(ctx):
    checkw(ctx.author.id)
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)

    if randomizecolor:
        embed = discord.Embed(color=discord.Color.random(), description=f"Prefix: {prefix} | Walter's selfbot - https://github.com/ProYT303/walterselfbot | Tehc Suport : https://discord.gg/kuSzstZyFf")
    else:
        embed = discord.Embed(color=embedcolor, description=f"Prefix: {prefix} | Walter's selfbot - https://github.com/ProYT303/walterselfbot | Tehc Suport : https://discord.gg/kuSzstZyFf")
    embed.add_field(name="utilities", value="ping,spam,imageembed,embed,avatar,nitro,webhook,playing,watching,listening,streaming,statusclear,ghostping,dmspam ", inline=False)
    embed.add_field(name="media", value="trump,recaptcha,clyde,deepfry,bobux", inline=True)
    embed.add_field(name="etc", value="shutdown,website,coinflip,uptime,loopnick,disableloopnick", inline=True)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
    args = list(args)
    spl = " ".join(args) 
    if spl:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=spl))
        await ctx.send(embed=embedsuccess('Success!'))
    else:
        await ctx.send(embed=embederror("What ya gonna listen to"))
@bot.command( aliases=['play'])
async def playing(ctx, *args):
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
    args = list(args) 
    try:
        await bot.change_presence(activity=discord.Game(name=""))
        await ctx.send(embed=embedsuccess('Successfully cleared status!'))
    except:
        await ctx.send(embed=embederror('Failed!'))

@bot.command( aliases=['watching'])
async def watch(ctx, *args):   
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
    r = requests.get('https://raw.githubusercontent.com/ProYT303/walterselfbot/main/ver')
    await ctx.send(f"""Version: {versione}
Newest version : {r.content.decode('utf8')}""")

@bot.command( aliases=['nitrogen'])
async def nitro(ctx, *args):   
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
    invcode = "kuSzstZyFf"
    r = requests.post(f"https://discord.com/api/v8/invites/{invcode}",headers={'authorization':token})
    print(r)
    if r.content:
        await ctx.send(embed=embedsuccess(f"Joined Support Server!"))
    else:
        await ctx.send(embed=embederror("failed successfully."))
@bot.command( aliases=['hax'])
async def hack(ctx, *args): 
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)  
    if user:
        await user.edit(nick=" ".join(args))
        await ctx.send(embed=embedsuccess('Successfully changed nickname!'))
    else:
        await ctx.send(embed=embederror(' Usage: ```nick mention/userid <new name>```'))

@bot.command( aliases=['joinserver'])
async def join(ctx, *args ):      
    checkw(ctx.author.id)
    invcode = args[0].replace('https://', "").replace('http://', "").replace('discord.gg/', "").replace('discord.com/invite/', "")
    r = requests.post(f"https://discord.com/api/v8/invites/{invcode}",headers={'authorization':token})
    if r == 200:
        await ctx.send(embed=embederror(f"Joined!"))
    else:
        await ctx.send(embed=embederror("Join command failed successfully."))
@bot.command( aliases=['memegen'])
async def meme(ctx, *args):      
    checkw(ctx.author.id)
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
@bot.command( aliases=['cyclenick', 'nickloop'])
async def loopnick(ctx, *args):     
    checkw(ctx.author.id) 
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
    checkw(ctx.author.id)     
    ln.cancel()
    if ctx.author.id != bot.user.id:
        return
    await ctx.author.edit(nick="")
    await ctx.send(embed=embedsuccess('Stopped!'))
@bot.command( aliases=['webhooksend', 'sendwebhook'])
async def webhook(ctx, *args):      
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    await ctx.send(text)
@bot.command(case_insensitive=True)
async def coinflip(ctx, *args):  
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
    await ctx.send('Shutting down the bot..')
    exit()
@bot.command(case_insensitive=True)
async def clyde(ctx, *args):  
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
    try:
        await ctx.message.delete()
    except:
        print(bcolors.WARNING + "No delete perms" + bcolors.ENDC)
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
        await ctx.send(embed=e)
    else:
        await ctx.send(asci)
@bot.command(case_insensitive=True)
async def embed(ctx, *args):   
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
    try:
        await ctx.message.delete()
    except:
        print('no delete perms smh')
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
    checkw(ctx.author.id)
    await ctx.message.delete()
    a = await ctx.send('┬─┬ ノ( ゜-゜ノ)')
    await asyncio.sleep(0.5)
    await a.edit(content='(╯°□°）╯︵ ┻━┻')
@bot.command(aliases=['dmspam'])
async def spamdm(ctx, member: discord.Member = None, *args):
    checkw(ctx.author.id)
    await ctx.message.delete()
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
    checkw(ctx.author.id)
    if args:
        await bot.change_presence(activity=discord.Streaming(name=" ".join(args), url='https://www.youtube.com/watch?v=iik25wqIuFo&feature=emb_title'))
        await ctx.send(embed=embedsuccess('Successfully changed status!'))
    else:
        await ctx.send(embed='What should ya stream?')
@bot.command(aliases=['dogecoinbalance', 'dogecoinbal'])
async def dogebal(ctx,*args):
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
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
    checkw(ctx.author.id)
    link = f"https://dogechain.info/chain/Dogecoin/q/totalbc"

    r = requests.get(link, allow_redirects=True)
    r = r.content.decode('utf8')
    if randomizecolor:
        e = discord.Embed(color=discord.Color.random(), title=f"Dogecoin mined total : {r}")
    else: 
        e = discord.Embed(color=embedcolor, title=f"Dogecoin mined total : {r}")
    await ctx.send(embed=e)
        



bot.run(token, bot=False)
