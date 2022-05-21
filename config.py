def best_server():
    servers = [
        "https://searx.org/search",
        "https://jsearch.pw/searx/search",
        "https://timdor.noip.me/searx/search",
        "https://searx.run/search",
        "https://searx.sethforprivacy.com/search",
        "https://searx.kujonello.cf/search"
    ]
    
    return servers


# хостер SearX, взятый с сайта - https://searx.space/
search_domain = best_server()

# OnionSearchEngine - поисковик, использующий Tor Exit Node, для функции анонимайзера/веб-прокси
anonimayzer_domain = "https://onionsearchengine.com/url.php?u="

use_anonimayzer = True