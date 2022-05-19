import telebot
from telebot import types
import requests


from config import token


bot = telebot.TeleBot(token, parse_mode=None) 



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):


    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Напишите ваш запрос", reply_markup=a)
    
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    r = requests.get("https://searx.prvcy.eu/search?q={}&format=json&safesearch=1".format(message.text))
    markup = types.InlineKeyboardMarkup()
    for i in range(0, 5):
        try:
            webAppTest = types.WebAppInfo(r.json()["results"][i]["url"]) #создаем webappinfo - формат хранения url
            markup.row(types.InlineKeyboardButton(r.json()["results"][i]["title"], web_app=webAppTest))
        except: pass
        
    headers = {
        'authority': 'api.duckduckgo.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.132 YaBrowser/22.3.1.922 Yowser/2.5 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'ru,en;q=0.9',
    }

    
    params = {
        'q': message.text,
        'format': 'json',
    }

    response = requests.get('https://api.duckduckgo.com/', params=params, headers=headers)
    
    bot.send_message(message.chat.id, "Быстрый ответ\n\n" + str(response.json()["Abstract"]), reply_markup=markup)


#time.sleep(1)
bot.remove_webhook()
bot.infinity_polling()