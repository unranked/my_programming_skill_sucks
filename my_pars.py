import requests
import bs4


def fixed_url(url):
    return url


def valid_url(url):
    return True


def main():

    url = input()
    url = fixed_url(url)
    if not valid_url(url):
        exit("Невозможно получить информацию с данного URL")

    html_doc = requests.get(url).content.decode('utf-8')
    soup = bs4.BeautifulSoup( html_doc, 'html.parser')
    table = soup.find('div', class_='b-topic__content');
    for row in table.find_all('h1'):
        for item in row.find_all('a'):
            item = item.text

    for row in table.find_all('p'):
        for item in row.find_all('a'):
            item = item.text
    for row in table.find_all('h1'):
        print(row.text)
    for row in table.find_all('p'):
        print(row.text)


if __name__ == '__main__':
    main()