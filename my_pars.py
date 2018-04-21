from configure import *
import requests
import bs4

def valid_url(url):
    return True


def main():
    print(hello_word)

    ans = int(input())

    if ans == 0:
        exit("Для поддержки программой нового сайта попробуйте написать разработчику\n"
             "на электронную почту can.do.attitute@gmail.com и ожидайте обновления на GitHub.")
    elif ans < 0 or ans > item_count:
        exit("Некорректный ввод!")

    url = input()               # Вводим URL
    url = ''.join(url.split())  # Избавляемся от неожиданных пробелов в данном пользователем URL
    if not valid_url(url):      # Проверяем, можем ли мы получить доступ к ссылке, а так же корректно ли она написана
        exit("Невозможно получить информацию с данного URL")

    html_doc = requests.get(url).content.decode('utf-8')
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')

    all_content = config[ans]
    tag, where = all_content["where"]
    content = all_content["text"]
    table = soup.find(tag, class_=where)

    for temp in content:
        for row in table.find_all(temp):
            for item in row.find_all('a'):
                item = item.text

    for temp in content:
        for row in table.find_all(temp):
            print(row.text)


if __name__ == '__main__':
    main()
