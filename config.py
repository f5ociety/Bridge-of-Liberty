def best_server():
    servers = [
        "http://908865-cu13401.tmweb.ru/searx/search", ## СЕРВЕР КОМАНДЫ CLAY
        "https://searx.org/search",
        "https://timdor.noip.me/searx/search",
        "https://searx.run/search",
        "https://searx.sethforprivacy.com/search",
        "https://searx.kujonello.cf/search",
        "https://searx.nevrlands.de/searx/search",
        "https://searx.divided-by-zero.eu/search",
        "https://searx.bissisoft.com/search",
        "https://search.jpope.org/search",
        "https://searx.sp-codes.de/search"
    ]
    
    return servers


# хостер SearX, взятый с сайта - https://searx.space/
search_domain = best_server()

# OnionSearchEngine - поисковик, использующий Tor Exit Node, для функции анонимайзера/веб-прокси
anonimayzer_domain = "http://213.226.127.137:5000/anon/?query="

use_anonimayzer = True

# поисковой движок для поиска
# Оффициальная документация SearX - https://searx.github.io/searx/dev/search_api.html
# уставьте пустым, если хотите использовать движки, которые по умолчанию поставил администратор сервера searx
# названия поисковых систем возьмите отсюда - https://searx.be/preferences
# можно поставить all и тогда будет искаться по всем доступным движкам
search_engines = "duckduckgo"
search_locales = "ru" #язык поиска, оставьте пустым, если хотите использовать язык, который по умолчанию поставил администратор сервера searx
savesearch = 0 # безопасный поиск. 1 - включен


startMessage = '''Этот бот использует несколько технологий, чтобы предоставить доступ к заблокированному ресурсу. 

Введите запрос как в обычный поисковик и получите ответ.

Отправьте боту ссылку(обязательно с "https://" в начале), чтобы открыть её внутри Telegram

Поиск по новостям: отправьте боту сообщение вида "news:новости в мире" и вы будете искать по категории "Новости"
'''