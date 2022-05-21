import telebot
from telebot import types
import requests
import json
import ast


from config import search_domain, anonimayzer_domain, use_anonimayzer, startMessage
from tokens import token_telegram


bot = telebot.TeleBot(token_telegram, parse_mode=None) 

global r


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):


    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, startMessage, reply_markup=a)
    
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    
    
    ### ОБРАБОТКА ССЫЛКИ - ОТКРЫТИЕ ССЫЛКИ ЛЮБЫМ ДОСТУПНЫМ СПОСОБОМ
    if message.text.startswith("http://") or message.text.startswith("https://"):
        
        # ПЕРЕВОДИМ САЙТ В HTTPS
        url: str = message.text
        url = url.replace("http://", "https://", 1)
        
        #---------------------
        # СОЗДАЕМ КНОПКИ
        markup = types.InlineKeyboardMarkup()
        
        webAppTest = types.WebAppInfo(url) #создаем webappinfo - формат хранения url
        markup.row(types.InlineKeyboardButton(url, web_app=webAppTest))
        
        webAppTest = types.WebAppInfo(anonimayzer_domain + url) #создаем webappinfo - формат хранения url
        markup.row(types.InlineKeyboardButton("Открыть в анонимайзере", web_app=webAppTest))
        
        webAppTest = types.WebAppInfo("https://webcache.googleusercontent.com/search?q=cache:" + url) #создаем webappinfo - формат хранения url
        markup.row(types.InlineKeyboardButton("Google Cache", web_app=webAppTest))
        
        webAppTest = types.WebAppInfo("https://web.archive.org/web/" + url) #создаем webappinfo - формат хранения url
        markup.row(types.InlineKeyboardButton("Web Archive", web_app=webAppTest))
        
        bot.send_message(message.chat.id, '[Открыть в браузере\n](' + url + ')', reply_markup=markup, parse_mode="markdown")
        #-------------------------
        
    ### ПОИСК ИНФОРМАЦИИ В ПОИСКОВОЙ СИСТЕМЕ
    else:
        r = requests.get(search_domain[0] + "?q={}&format=json&safesearch=0&locales=ru".format(message.text))
        
        
        ### ЕСЛИ API ЗАБАНЕН, ТО МЕНЯЕМ API ИЗ СПИСКА И ПОЛУЧАЕМ ОТВЕТ
        i = 0
        while(r.text == "Rate limit exceeded"):
            i = i + 1
            r = requests.get(search_domain[i] + "?q={}&format=json&safesearch=0&locales=ru&engines=duckduckgo".format(message.text))
            print("поменял api на " + search_domain[i])
            print(r.text)
        

        with open("users/" + str(message.chat.id) + ".json", "w", encoding="utf-8") as f:
            print(type(r.json()))
            print("-----------")
            f.write(str(r.json()))
        #-------------------------
        ## СОЗДАЕМ КНОПКИ
        markup = types.InlineKeyboardMarkup()
        for i in range(0, 8):
            try:
            
                print(r.json()["results"][i]["url"])
                ### УБИРАЕМ ВСЕ bing.com ссылки
                if(("bing.com" in r.json()["results"][i]["url"]) == False):
                    markup.row(types.InlineKeyboardButton(r.json()["results"][i]["url"], callback_data=str(i)))
            except:
                pass
            
            

            
            
        ### БЫСТРЫЙ ОТВЕТ ОТ DUCKDUCKGO ###    
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
        ###-------------------------------------
        
        bot.send_message(message.chat.id, "Провайдер " + search_domain[i] + "\nБыстрый ответ\n\n" + str(response.json()["Abstract"]), reply_markup=markup)
        #bot.send_message(message.chat.id, "Быстрый ответ\n\n", reply_markup=markup)

''' ЭТА ШТУКА НЕ РАБОТАЕТ
@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    print(call.data)

    bot.send_message(call.message.chat.id, '{}'.format(str(call.data)))
    bot.answer_callback_query(call.id)
    '''
    
### ДЛЯ ИЗМЕНЕНИЯ СООБЩЕНИЯ
@bot.callback_query_handler(lambda call: True)
def handle(call):

    if(call.data == "back"):
        
        with open("users/" + str(call.message.chat.id) + '.json', encoding="utf-8") as f:
            d = f.read()
            js = ast.literal_eval(d)
        #-------------------------
        ## СОЗДАЕМ КНОПКИ
        markup = types.InlineKeyboardMarkup()
        for i in range(0, 8):
            if use_anonimayzer:
                webAppTest = types.WebAppInfo(anonimayzer_domain +  js["results"][i]["url"]) #создаем webappinfo - формат хранения url
            else:
                url: str = js["results"][i]["url"]
                if url.startswith("http://"):
                    url = url.replace("http://", "https://", 1)
                        
                    webAppTest = types.WebAppInfo(url) #создаем webappinfo - формат хранения url
                else:
                    webAppTest = types.WebAppInfo(r.json()["results"][i]["url"]) #создаем webappinfo - формат хранения url
                    
            #markup.row(types.InlineKeyboardButton(r.json()["results"][i]["url"], web_app=webAppTest))
            #markup.row(types.InlineKeyboardButton(r.json()["results"][i]["title"], callback_data=json.dumps({"key":"value"})))
            
            markup.row(types.InlineKeyboardButton(js["results"][i]["url"], callback_data=str(i)))
            
        ### БЫСТРЫЙ ОТВЕТ ОТ DUCKDUCKGO ###    
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
            'q': js["query"],
            'format': 'json',
        }
        response = requests.get('https://api.duckduckgo.com/', params=params, headers=headers)
        ###-------------------------------------
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Провайдер " + search_domain[i] + "\nБыстрый ответ\n\n" + str(response.json()["Abstract"]), reply_markup=markup)
    
    else:
    
        #print(call.message.json["reply_markup"]["inline_keyboard"][int(call.data)][0]["text"])
        '''
        with open("users/" + str(call.message.chat.id) + '.json', encoding="utf-8") as f:
            d = f.read()
            js = ast.literal_eval(d)'''
        
        # ПЕРЕВОДИМ САЙТ В HTTPS
        #url: str = js["results"][int(call.data)]["url"]
        url: str = call.message.json["reply_markup"]["inline_keyboard"][int(call.data)][0]["text"]
        url = url.replace("http://", "https://", 1)
            
        #---------------------
        # СОЗДАЕМ КНОПКИ
        markup = types.InlineKeyboardMarkup()
            
        webAppTest = types.WebAppInfo(url) #создаем webappinfo - формат хранения url
        markup.row(types.InlineKeyboardButton(url, web_app=webAppTest))
            
        webAppTest = types.WebAppInfo(anonimayzer_domain + url) #создаем webappinfo - формат хранения url
        markup.row(types.InlineKeyboardButton("Открыть в анонимайзере", web_app=webAppTest))
            
        webAppTest = types.WebAppInfo("https://webcache.googleusercontent.com/search?q=cache:" + url) #создаем webappinfo - формат хранения url
        markup.row(types.InlineKeyboardButton("Google Cache", web_app=webAppTest))
            
        webAppTest = types.WebAppInfo("https://web.archive.org/web/" + url) #создаем webappinfo - формат хранения url
        markup.row(types.InlineKeyboardButton("Web Archive", web_app=webAppTest))
        
        markup.row(types.InlineKeyboardButton("Назад", callback_data=str("back")))
            
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='[Открыть в браузере\n](' + url + ')', reply_markup=markup, parse_mode="markdown")
        #-------------------------

        '''
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=call.data)
        bot.answer_callback_query(call.id)'''

#time.sleep(1)
bot.remove_webhook()
bot.infinity_polling()