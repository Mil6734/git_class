import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    res = requests.get(url)
    return res.text


def write_csv(data):
    with open('news.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow((data['time'], data['news'], data['href']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    nw = soup.find_all('div', class_="se-news-list-page__item")[:12]
    # print(nw)
    for i in nw:
        try:
            time = i.find('div', class_="se-news-list-page__item-left").text.strip()
        except ValueError:
            time = ''
        # print(name)

        try:
            news = i.find('div', class_='se-material__title').text.strip()
        except ValueError:
            news = ''
        # print(news)

        try:
            href = i.find('div', class_='se-material__title').find('a').get('href')
        except ValueError:
            href = ''
        # print(href)

        data = {
            'time': time,
            'news': news,
            'href': href
        }
        write_csv(data)


def main():
    url = "https://www.sport-express.ru/football/transfers/news/"
    get_data(get_html(url))


if __name__ == '__main__':
    main()
