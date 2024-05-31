import colorama, datetime, requests, sys, json, os, random, time, threading, base64, youtube_dl, discord, asyncio
from colorama import Fore
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
ffmpeg_options = {
    'options': '-vn'
}
def return_glitch():
    payload = {
    'theme': "dark",
    'locale': "ja",
    'message_display_compact': False,
    'enable_tts_command': False,
    'inline_embed_media': True,
    'inline_attachment_media': False,
    'gif_auto_play': False,
    'render_embeds': False,
    'render_reactions': False,
    'animate_emoji': False,
    'convert_emoticons': False,
    'explicit_content_filter': '0',
    'status': "invisible"
    }
    return payload
def leave_guild(headers,id):
    while True:
        src = requests.delete(f'https://canary.discordapp.com/api/v6/users/@me/guilds/{id}', headers=headers ,timeout=20)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
def delete_guild(headers,id): 
    while True:
        src = requests.delete(f'https://canary.discordapp.com/api/v6/users/@me/guilds/{id}', headers=headers ,timeout=20)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
def remove_friend(id,headers):
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v6/users/@me/relationships/{str(id)}", headers=headers, timeout=10)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
def create_guild(name,headers):
    payload = {"name": name}
    while True:
        src = requests.post(f'https://canary.discordapp.com/api/v6/guilds', headers=headers, json=payload, timeout=10)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
def close(id,headers):
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v6/channels/{id}", headers=headers, timeout=10)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


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
      {Fore.RED}sipher#6969 | @siph.er | github.com/siph-er{Fore.RESET}

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