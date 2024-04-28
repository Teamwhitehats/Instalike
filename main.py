import telebot
import random
import string
import time
import names
import requests
HTTP = requests
proxy_url = None
proxies = None #{'http': proxy_url, 'https': proxy_url}
proxy_list = [
    '14.237.78.172:443',
    '26.219.24.169:21',
    '152.120.6.174:512',
    '149.255.225.12:445',
    '166.83.92.137:8080',
    '188.49.80.198:445',
    '200.241.220.204:514',
    '125.164.187.108:514',
    '65.40.17.213:22',
    '64.46.161.97:4444',
    '40.85.196.43:111',
    '66.91.132.112:8080',
    '155.116.113.76:1524',
    '213.100.140.82:23'
]

proxy = random.choice(proxy_list)
def get_headers(Country,Language):
    while True:
        try:
            an_agent=f'Mozilla/5.0 (Linux; Android {random.randint(9,13)}; {"".join(random.choices(string.ascii_uppercase, k=3))}{random.randint(111,999)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'


            res = requests.get("https://www.facebook.com/",headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'},proxies=proxies, timeout=30)
            js_datr = res.text.split('["_js_datr","')[1].split('",')[0]
            r=requests.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers={
                'user-agent': an_agent
            },proxies=proxies,timeout=30).cookies

            headers1 = {
                'authority': 'www.instagram.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={js_datr}',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': an_agent,
                'viewport-width': '980',
            }
            response1 = requests.get('https://www.instagram.com/', headers=headers1,proxies=proxies,timeout=30)
            appid=response1.text.split('APP_ID":"')[1].split('"')[0]
            rollout=response1.text.split('rollout_hash":"')[1].split('"')[0]
            headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': f'{Language}-{Country},en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'dpr=3; csrftoken={r["csrftoken"]}; mid={r["mid"]}; ig_nrcb=1; ig_did={r["ig_did"]}; datr={js_datr}',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/signup/email/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': an_agent,
                'viewport-width': '360',
                'x-asbd-id': '198387',
                'x-csrftoken': r["csrftoken"],
                'x-ig-app-id': str(appid),
                'x-ig-www-claim': '0',
                'x-instagram-ajax': str(rollout),
                'x-requested-with': 'XMLHttpRequest',
                'x-web-device-id': r["ig_did"],
            }
            return headers
        except Exception as E:
            print(E)
headers=get_headers(Country='US',Language='en')    
def Get_UserName(Headers,Name,Email):
    try:

        updict = {"referer": 'https://www.instagram.com/accounts/signup/birthday/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}
        while True:


            data = {
                'email': Email,
                'name': Name+str(random.randint(1,99)),
            }

            response = requests.post(
                'https://www.instagram.com/api/v1/web/accounts/username_suggestions/',
                headers=Headers,
                data=data,
                proxies=proxies,
                timeout=30
            )
            if 'status":"fail' in response.text:
                print(response.text)
            elif 'status":"ok' in response.text :
                print("   Success   ")
                return random.choice(response.json()['suggestions'])
            else:print(response.text)

    except Exception as E:
        print(E)


def Send_SMS(Headers,Email):
    try:
        data = {
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email,
}

        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/send_verify_email/',
            headers=Headers,
            data=data,
            proxies=proxies,
            timeout=30
        )
        return response.text
    except Exception as E:
        print(E)



def Validate_Code(Headers,Email,Code):

    try:
        updict = {"referer": 'https://www.instagram.com/accounts/signup/emailConfirmation/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}



        data = {
            'code': Code,
            'device_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'email': Email,
        }

        response = requests.post(
            'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
            headers=Headers,
            data=data,
            proxies=proxies,
            timeout=30
        )
        return response



    except Exception as E:
        print(E)



def Create_Acc(Headers,Email,SignUpCode):

    try:
        firstname=names.get_first_name()
        UserName=Get_UserName(headers,firstname,Email)
        Password=firstname.strip()+'@'+str(random.randint(111,999))

        updict = {"referer": 'https://www.instagram.com/accounts/signup/username/'}
        Headers = {key: updict.get(key, Headers[key]) for key in Headers}


        data = {
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{round(time.time())}:{Password}',
            'email': Email,
            'username': UserName,
            'first_name': firstname,
            'month': random.randint(1,12),
            'day': random.randint(1,28),
            'year': random.randint(1990,2001),
            'client_id': Headers['cookie'].split('mid=')[1].split(';')[0],
            'seamless_login_enabled': '1',
            'tos_version': 'row',
            'force_sign_up_code': SignUpCode,
        }


        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
            headers=Headers,
            data=data,
            proxies=proxies,
            timeout=30

        )
        print(response.text)
        if '"account_created":true' in response.text:
            print('UserName : ' + UserName)
            print('PassWord : ' + Password)
            print('Sessionid : ' +response.cookies['sessionid'])
            return f'{UserName}:{Password}'
        else:
            pass
    except Exception as E:
        print(E)        
bot = telebot.TeleBot('7096049387:AAGF87KeLj-z5d6NECUIcBjyJe7vZw2JSSE') 
print(bot.get_me())
users = {}
import json
import time
import json

def extract_otp_from_json(json_response):
    e = json_response
    for i in e:
        e = i['subject']
        e = e.replace(' is your Instagram code','')
        print(e)            
    return e    
def get_email_messages(at):
    while True:
        json_dataa = requests.get(f"https://api.internal.temp-mail.io/api/v3/email/{at}/messages").json()
        if str(json_dataa) == str([]):
            print("Retrying...")
            time.sleep(1)
        else:
            return json_dataa       
@bot.message_handler(commands=['create'])
def start(message):    
    content = HTTP.post("https://api.internal.temp-mail.io/api/v3/email/new",
    json={'min_name_length': 10, 'max_name_length': 10}).json()
    result = content
    c1 = result['email']
    c2 = result['token']
    email = c1
    Email = email
    at = Email
    time.sleep(10)
    users[message.from_user.id] = email     
    ss=Send_SMS(headers,Email)
    if 'email_sent":true' in ss:
        json_dataa = get_email_messages(at)
        bot.reply_to(message,json_dataa)
        code = extract_otp_from_json(json_dataa)
        a=Validate_Code(headers,Email,code)
        if 'status":"ok' in a.text:
            SignUpCode=a.json()['signup_code']            
            dict = Create_Acc(headers,Email,SignUpCode)
            print(dict)
            if dict is not None:
                a = dict.split(':')
                bot.reply_to(message,f'Email : {a[0]}\nPassword : {a[1]}')
            else:
                bot.reply_to(message,f'Error')
        else:
            print( "Done, TG : @princemodder")
    else:
        pass
bot.infinity_polling()        
