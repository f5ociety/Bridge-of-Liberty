def best_server():
    servers = [
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
anonimayzer_domain = "https://onionsearchengine.com/url.php?u="

use_anonimayzer = True

startMessage = '''Этот бот использует несколько технологий, чтобы предоставить доступ к заблокированному ресурсу. 

Введите запрос как в обычный поисковик и получите ответ.

Отправьте боту ссылку(обязательно с "https://" в начале), чтобы открыть её внутри Telegram'''