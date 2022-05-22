# Telegram-Search-Bot (Мост Свободы)
Проект для Хакатона от [**РосКомСвободы**](https://roskomsvoboda.org/) ([**demhack 4**](https://demhack.ru/)).

Телеграм Бот для поиска и просмотра информации прямо внутри мессенджера.

[**Презентация**](https://prezi.com/view/G3njJpYCAbd5TfYvoowI/)

# Как работает Telegram Bot?
Мы используем [**DuckDuckGo API**](https://api.duckduckgo.com/api) для быстрых ответов и поисковую систему **SearX** через которую мы также собираем ответы, у нас несколько хостеров, которых мы взяли для демо-представления. 

Вы делаете запрос боту, и он вам возвращает вам список ссылок (5 штук), нажав на одну вы поподаете на карточку сайта (некоторые сайты есть в виде [**Instant View**](https://instantview.telegram.org/), таким образом вы сможете прочитать сразу, не переходя на сайт), где можете выбрать метод открытия сайта - с Анонимайзера, с помощью [**Web Archive**](https://archive.org/web/) или с помощью других иструментов, которые мы дполним позже.

Сам Телеграм выступает в качестве хранилища и умеет держит в памяти ранее открытые **Instant View** ссылки (функция оффлайн просмотра), также в instant view карточках отсутствует **JavaScript**, что делает просмотр страниц в разы анонимнее.

# Beta Version
Для Beta версии бота мы используем [**Onion search engine**](https://addons.mozilla.org/ru/firefox/addon/onion-search-engine/), которая позволяет нам предложить такую функцию как - "открыть через анонимайзер" и SearX хостеров ([**https://searx.space/**](https://searx.space/)), которая используется для выдачи обычых ответов. 

# Инструменты
**Для бота:**
- Python
- [**DuckDuckGo API**](https://api.duckduckgo.com/api)
- [**PyTelegramBot**](https://github.com/eternnoir/pyTelegramBotAPI)
- [**SearXNG**](https://github.com/searxng/searxng) и [**SearX**](https://github.com/searx/searx)
- [**Telegram Bots**](https://core.telegram.org/bots)
- [**Web Archive**](https://archive.org/web/)
- и другие инструменты, которые мы пока внедряем 

**Для сайта:** 
- **HTML**
- **CSS (+SCSS)**

# Команда (CLAY - Clowns Laughing At You)
- **LencoDigitexer** (Telegram Bot + Pitching)
- **SeryiBaran** (Frontend + license)
- **Erghel** (Frontend + Documentation)

# Будущее
- [ ] развернем YaCy и SearX на своих серверах, отказавшись от посторинник хостеров 
- [ ] развернем свой Анонимайзер, чтобы отказаться от постороннего 
- [x] сделаем карточки для каждого сайта из выдачи
- [x] сделаем красивый веб-сайт, которые познакомит пользователя с ботом 
