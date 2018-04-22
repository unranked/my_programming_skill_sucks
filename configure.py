
# Настройка парсера/форматирования

#
# width - длина строки в отформатированном тексте.
#

width = 80

#
# item_count - количество сайтов, с которыми программа на данный момент может работать
#

item_count = 6

#
# hello_word - приветсвенное слово, которое видит
# пользователь при запуске скрипта.
# Допустимо изменение при добавлении нового сайта в список.
#

hello_word = "---***---***---***---***---***---***---***---***---***---\n" \
             "Выберите сайт(его номер в списке),\n" \
             "из страницы которого Вы хотели бы получить текстовый файл.\n" \
             "0. Не могу найти нужный мне сайт.\n" \
             "1. Лента         - lenta.ru\n" \
             "2. Газета        - gazeta.ru\n" \
             "3. РИА Новости   - ria.ru\n" \
             "4. 76.RU Новости - 76.ru\n" \
             "5. Вести         - vesti.ru\n" \
             "6. ЯР Новости    - yarnovosti.com\n" \
             "---***---***---***---***---***---***---***---***---***---\n"

#
# config - указания мест, откуда желательно вытаскивать информацию нашему парсеру
# "where": блок, где сконцентрирована основная информация. Его поиск осуществляется вручную.
# "text": список тегов, в которых есть информация в виде текста. Всё тоже вручную(обидно).
#

config = [
    "NOTHING",
    {
        "where": ("div", "b-topic__content"),                   # elem 1
        "text": ["h1", "p"],
        "encoding": "utf-8"
    }, {
        "where": ("article", "main_article b-article"),         # elem 2
        "text": ["h2", "h1", "p"],
        "encoding": "cp1251"
    }, {
        "where": ("div", "b-article__ind"),                     # elem 3
        "text": ["h1", "p"],
        "encoding": "utf-8"
    }, {
        "where": ("div", "news-record copyright-insert"),       # elem 4
        "text": ["h1", "p"],
        "encoding": "cp1251"
    }, {
        "where": ("div", "article"),                            # elem 5
        "text": ["h3", "p"],
        "encoding": "utf-8"
    }, {
        "where": ("div", "_content"),                           # elem 6
        "text": ["h1", "p"],
        "encoding": "utf-8"
    }
]