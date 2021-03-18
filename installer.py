import os

import requests as r # on compiling, make sure y have requests in the folder.
print("Installing Required modules..")
if os.name == "nt":
    os.system("py -3 -m pip install requests discord.py")
else:
    os.system("python3 -m pip install requests discord.py")
print('Done!')

print("Downloading ")
rr = r.get("https://raw.githubusercontent.com/ProYT303/walterselfbot/main/index.py", allow_redirects=True)
cont = rr.content
f = open('index.py', 'wb')
f.write(cont)
if os.name == "nt":
    f = open('start.bat', 'w')
    f.write('py -3 index.py')
    do = "double click start.bat"
else:
    f = open('start.sh', 'w')
    f.write('python3 index.py')
    do = "open start.sh"
print(f"Successfully downloaded walter's selfbot. please {do}")
input()
