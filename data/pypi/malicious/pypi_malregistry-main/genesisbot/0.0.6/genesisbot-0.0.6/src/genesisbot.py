import colorama, datetime, requests, sys, json, os, random, time, threading, base64
from colorama import Fore
def clear():
    if sys.platform == "win32" or sys.platform == "win64":
        os.system("cls")
    else:
       os.system("clear")
def flood(sock, ip, port, stop, bytes):
    while time.time() < stop:
        sock.sendto(bytes, (ip,port))
def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc
def ui(auth):
    config = json.loads(open('assets/config.json','r').read())
    headers = {'authorization' : auth}
    response = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers, timeout=10).json()
    friends = requests.get("https://canary.discordapp.com/api/v6/users/@me/relationships", headers=headers, timeout=10).json()
    servers = requests.get('https://canary.discordapp.com/api/v6/users/@me/guilds', headers=headers, timeout=10).json()
    dm_channels = requests.get('https://canary.discordapp.com/api/v6/users/@me/channels', headers=headers, timeout=10).json()
    print(f"""
{Fore.CYAN}


  ▄████ ▓█████  ███▄    █ ▓█████   ██████  ██▓  ██████ 
 ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▓██▒▒██    ▒ 
▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ░ ▓██▄   ▒██▒░ ▓██▄   
░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒░██░  ▒   ██▒                Prefix: {config['prefix']}
░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒▒██████▒▒░██░▒██████▒▒
 ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░▓  ▒ ▒▓▒ ▒ ░
  ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ▒ ░░ ░▒  ░ ░
░ ░   ░    ░      ░   ░ ░    ░   ░  ░  ░   ▒ ░░  ░  ░  
      ░    ░  ░         ░    ░  ░      ░   ░        ░ 
{Fore.RESET}
      {Fore.RED}xin#1111 | @siph.er | github.com/devil-xin{Fore.RESET}

[{Fore.YELLOW}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] Information on {Fore.WHITE}{response['username']}#{response['discriminator']}{Fore.RESET}:

[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] Name: {Fore.WHITE}{response['username']}#{response['discriminator']}{Fore.RESET}
[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] ID: {Fore.WHITE}{response['id']}{Fore.RESET}
[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] Email: {Fore.WHITE}{response['email']}{Fore.RESET}
[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] Phone: {Fore.WHITE}{response['phone']}{Fore.RESET}
[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] Friends: {Fore.WHITE}{len(friends)}{Fore.RESET}
[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] Servers: {Fore.WHITE}{len(servers)}{Fore.RESET}
[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] DM Channels: {Fore.WHITE}{len(dm_channels)}{Fore.RESET}
[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] OS Platform: {Fore.WHITE}{sys.platform}{Fore.RESET}

{Fore.RESET}""")
    src = requests.post('https://canary.discord.com/api/v6/invite/ry9ZQ7K',headers={'authorization' : auth},timeout=10)
    try:
        print(f"[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] You have {Fore.RED}FAILED{Fore.RESET} to join the Genesis server, go join it urself: discord.gg/ry9ZQ7K")
    except Exception as e:
        print(f"[{Fore.GREEN}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Fore.RESET}] {Fore.WHITE}You have{Fore.RESET} {Fore.GREEN}SUCCESSFULLY JOINED{Fore.RESET} {Fore.WHITE}the Genesis server!{Fore.RESET}")
def webhook_spam(webhook, content):
    payload = {'content': content}
    requests.post(webhook, json=payload)
def encrypt(message,corruptchanname):
    for x in message.content:
        if random.randint(1,2) == 1:
            corruptchanname += asciigen(1)
        else:
            corruptchanname += x   
    return corruptchanname