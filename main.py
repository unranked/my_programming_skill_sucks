from cfg import *
from look_better import Format
import requests
import bs4

def is_valid(url):
    return True

def main():
    print(hello_word)

    ans = int(input())

    if ans == 0:
        exit("Для поддержки программой нового сайта попробуйте написать разработчику\n"
             "на электронную почту can.do.attitute@gmail.com и ожидайте обновления на GitHub.")
    elif ans < 0 or ans > item_count:
        exit("Некорректный ввод!")

    url = input()                           
    url = ''.join(url.split())              # Избавляемся от неожиданных пробелов в данном пользователем URL
    
    if not is_valid(url):                   # Проверяем, можем ли мы получить доступ к ссылке, а так же корректно ли она написана
        exit("Невозможно получить информацию с данного URL")
    
    file_name = input("Назовите имя файла с информацией.\n")
        
    settings = config[ans]                  # Достаём настройки для ans'ого новостного сервиса
    
    encode = requests.get(url).encoding     # Достаём кодировку прямо с серва, еее
    html_doc = requests.get(url).content.decode(encode)
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')

    tag, where = settings["where"]
    content = settings["text"]
    table = soup.find(tag, class_=where)

    for temp in content:                    # Обработка ссылок:
        for row in table.find_all(temp):    # На данном этапе разработки ссылки мы просто удаляем,
            for item in row.find_all('a'):  # оставляя просто текст.
                item = item.text            # Это можно исправить прямо в этой строчке, да..

    raw_text = []

    for temp in content:
        for row in table.find_all(temp):
            raw_text.append(row.text)

    sth = Format(raw_text, width)

    good_text = sth.done()

    my_file = open(file_name + ".txt", "w")
    for s in good_text:
        my_file.write(s + "\n")


if __name__ == '__main__':
    main()
