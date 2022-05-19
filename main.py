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
    print(r.json()["results"][0])
    markup = types.InlineKeyboardMarkup()
    for i in range(0, 5):
        webAppTest = types.WebAppInfo(r.json()["results"][i]["url"]) #создаем webappinfo - формат хранения url
        markup.row(types.InlineKeyboardButton(r.json()["results"][i]["title"], web_app=webAppTest))
        
    bot.send_message(message.chat.id, "Ваш запрос - " + message.text, reply_markup=markup)


#time.sleep(1)
bot.remove_webhook()
bot.infinity_polling()