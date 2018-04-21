from configure import *
import requests
import bs4

def is_valid(sth):
    return True

def main():
    print(hello_word)

    ans = int(input())

    if ans == 0:
        exit("Для поддержки программой нового сайта попробуйте написать разработчику\n"
             "на электронную почту can.do.attitute@gmail.com и ожидайте обновления на GitHub.")
    elif ans < 0 or ans > item_count:
        exit("Некорректный ввод!")

    url = input()                           # Вводим URL
    url = ''.join(url.split())              # Избавляемся от неожиданных пробелов в данном пользователем URL
    if not is_valid(url):                   # Проверяем, можем ли мы получить доступ к ссылке, а так же корректно ли она написана
        exit("Невозможно получить информацию с данного URL")

    settings = config[ans]                  # Достаём настройки для i'ого новостного сервиса

    html_doc = requests.get(url).content.decode(settings["encoding"])   # Получаю html-код из ссылки
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')                   # Преобразую в элемент типа BS

    tag, where = settings["where"]          # tag - тэг основного местонахожения основной информации, where - класс.      
    content = settings["text"]              # content - то, что мы достанем из html-кода
    table = soup.find(tag, class_=where)    # Ищем место, где это всё и расположено.

    for temp in content:                    # Обработка ссылок:
        for row in table.find_all(temp):    # На данном этапе разработки ссылки мы просто удаляем,
            for item in row.find_all('a'):  # оставляя просто текст.
                item = item.text            # Это можно исправить прямо в этой строчке, да..

    raw_text = []                           # А тут просто пихаем поабзацно весь текст
    
    for temp in content:                    #
        for row in table.find_all(temp):    # Точнее вот тут..
            raw_text.append(row.text)       #

    

if __name__ == '__main__':
    main()
