import requests
from time import time
from hashlib import md5
from user_agent import generate_user_agent
from random import randrange
import telebot
from telebot import types
import os
import threading
import random
ids=[]

tok = input("TOKEN : 7028436368:AAGPMCNdR69NYwzDYWq0m-Djg6kSk4QEMoM")
print("\033[1;32;40mRun ")
bot=telebot.TeleBot(tok)

L7N1 = types.InlineKeyboardButton(text =" Dev 🐉",url="t.me/Hackervipking")
L7N2 = types.InlineKeyboardButton(text=" Get List ⚡",callback_data="list")

@bot.message_handler(commands=['start'])
def get_message(message):
          but= types.InlineKeyboardMarkup()
          but.row_width = 2
          but.add(L7N1)
          but.add(L7N2)
          photo = "https://w0.peakpx.com/wallpaper/458/671/HD-wallpaper-instagram-red-logo-red-neon-lights-creative-red-abstract-background-instagram-logo-social-network-instagram.jpg"
          name_of_L7N = f"{message.from_user.first_name}"
          the_user  = f"t.me/{message.from_user.username}"
          text = f'''* Welcome ! * [{name_of_L7N}]({the_user}) * To Bot Get List Instagram Without Sessionid *'''
          bot.send_photo(message.chat.id,photo,text ,
 parse_mode="Markdown",reply_markup=but)

@bot.callback_query_handler(func=lambda call:True)
def work(call):
 if call.data=="list":
  fuck=bot.send_message(call.message.chat.id,text="*How Many User do You Want?  *",parse_mode="Markdown")
  bot.send_message(call.message.chat.id,text="*Send Number From 50 to 250 Only*",parse_mode="Markdown")
  bot.register_next_step_handler(fuck,get_username)
def get_id():
  usid=str(randrange(18000000,500000000))
  if usid not in ids:
    ids.append(usid)
    return usid
  else:
    get_id()
def get_username(message):
  num = message.text
  if len(num) >= 250 :
  	bot.send_message(message.chat.id,"*Choice Under 250 !!\n Send* /start *Again* ",parse_mode="Markdown")	
  idd = message.chat.id
  okk=0
  sent_message = bot.send_message(message.chat.id,"Get Usernames...")
  for _ in range(int(num)):
    	ed =""
    	try:
    	 usid=get_id()
    	 csrftoken = md5(str(time()).encode()).hexdigest()
    	 headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'dpr': '0.8',
    'origin': 'https://www.instagram.com',
    'user-agent': str(generate_user_agent()),
    'x-csrftoken': csrftoken,
    }
    	 data = {
    '__spin_b': 'trunk',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+usid+'","username":"0s9s"}',
    'server_timestamps': 'true',
    'doc_id': '7666785636679494',
}
    	 response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data).json()
    	 username=response['data']['user']['username']
    	 with open('list_ig_L7N.txt', 'a') as f:
    	 	f.write(username + '\n')
    	 	okk+=1
    	 	k2 = random.choice(["🕛","🕓","🕞","🕒","🕝","🕑","🕜","🕐","🕧","🕗","🕢","🕖","🕡","🕕","🕠","🕔","🕟","🕦","🕚","🕥","🕙","🕤","🕘","🕣"])
    	 	f.write(username + '\n')    	 	
    	 	ed += f"*Arrived To (*`{okk}`*/*`{num}`*) {k2}*"
    	 	bot.edit_message_text(chat_id=message.chat.id, message_id=sent_message.message_id, text=ed,parse_mode="Markdown")         
    	except Exception as e:pass     
  file = open('list_ig_L7N.txt', 'rb')
  bot.send_document(idd,file,caption=f"""
*Save ({okk}) User ✅*

*BY :* [𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™](t.me/Hackervipking)
    """,parse_mode="Markdown")
  file3 = 'list_ig_L7N.txt'
  os.remove(file3)

def bot_thread():
    if __name__ == '__main__':
        bot.polling(none_stop=True)
thread = threading.Thread(target=bot_thread)
thread.start()
