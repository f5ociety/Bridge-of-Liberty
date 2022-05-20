# Telegram-Search-Bot (Anticensorship service)
Проект для Хакатона от [**РосКомСвободы**](https://roskomsvoboda.org/) ([**demhack 4**](https://demhack.ru/)).

Телеграм Бот для поиска и просмотра информации прямо внутри мессенджера.

# Как работает Telegram Bot?
Мы используем [**DuckDuckGo API**](https://api.duckduckgo.com/api) для быстрых ответов и поисковую систему **SearXNG** через которую мы также собираем ответы. 

Вы делаете запрос боту, и он вам возвращает вам список ссылок (5 штук), нажав на одну вы поподаете на карточку сайта (некоторые сайты есть в виде [**Instant View**](https://instantview.telegram.org/), таким образом вы сможете прочитать сразу, не переходя на сайт), где можете выбрать метод открытия сайта - с помощью Proxy, развернутого на сервере [**Telegram Web Apps**](https://core.telegram.org/bots/webapps), с помощью [**Web Archive**](https://archive.org/web/) или с помощью других иструментов, которые мы дполним позже.

Сам Телеграм выступает в качестве **Proxy-сервера** и умеет хранить в памяти ранее открытые **Instant View** ссылки (функция оффлайн просмотра), также в instant view карточках отсутствует **JavaScript**, что делает просмотр страниц в разы анонимнее.

# Beta Version
Для Beta версии бота мы используем [**Onion search engine**](https://addons.mozilla.org/ru/firefox/addon/onion-search-engine/), которая позволяет нам предложить такую функцию как - "открыть через анонимайзер" и SearX хостера ([**https://searx.org/search**](https://searx.org/search)), которая используется для выдачи обычых ответов. 

# Инструменты
**Для бота:**
- Python
- [**DuckDuckGo API**](https://api.duckduckgo.com/api)
- [**PyTelegramBot**](https://github.com/eternnoir/pyTelegramBotAPI)
- [**SearXNG**](https://github.com/searxng/searxng) 
- [**Telegram Bots**](https://core.telegram.org/bots)
- [**Web Archive**](https://archive.org/web/)

**Для сайта:** 
- **HTML**
- **CSS**

# Команда (CLAY - Clowns Laughing At You)
- **LencoDigitexer** (Telegram Bot + Pitching)
- **SeryiBaran** (Frontend + license)
- **Erghel** (Frontend + Documentation)


