import time
import colorama
from colorama import Fore
import webbrowser
import json
import requests
import os
from colorama import init
init()
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
animation = [
"[        ]",
"[=       ]",
"[===     ]",
"[====    ]",
"[=====   ]",
"[======  ]",
"[======= ]",
"[========]",
"[ =======]",
"[  ======]",
"[   =====]",
"[    ====]",
"[     ===]",
"[      ==]",
"[       =]",
"[        ]",
"[        ]"
]

notcomplete = True

i = 0
def logo():
  print(Fore.YELLOW + """

██████╗  █████╗ ███████╗████████╗███████╗    ██╗  ██╗
██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝    ╚██╗██╔╝
██████╔╝███████║███████╗   ██║   █████╗       ╚███╔╝ 
██╔═══╝ ██╔══██║╚════██║   ██║   ██╔══╝       ██╔██╗ 
██║     ██║  ██║███████║   ██║   ███████╗    ██╔╝ ██╗
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝
                                                     
""")
time.sleep(1)
re = requests.get('http://evo-updater.glitch.me/pastex.htm')
if "1.5" not in r.text:
  input(Fore.GREEN + "Update avalible! Please update on Github")
  webbrowser.open_new(url="https://github.com/evo0616lution/PasteX/releases)
logo()
obj = input(Fore.RESET + "Paste text you want to upload:\n")
time.sleep(1)
cls()
logo()
print(Fore.LIGHTBLUE_EX + "Uploading...")
while notcomplete:
    print(animation[i % len(animation)], end='\r')
    time.sleep(.1)
    i += 1
    if i == 3*10:
      break
cls()
paste = "https://paste.agalts.xyz/upload?paste=" + str(obj)
try:
  r = requests.get(paste)
except:
  print(Fore.RED + "Upload failed. Check your internet connection and try again.")
x = r.text
y = json.loads(x)
logo()
print(Fore.GREEN + "Upload successful")
print(Fore.RESET + "\n")
print(y["url"])
pasteurl = y["url"]
time.sleep(0.4)
webbrowser.open_new(url=pasteurl)
print(Fore.CYAN + "\n")
input("Press enter to close the program.")
