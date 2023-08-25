import requests
from bs4 import BeautifulSoup


class Parser:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        reg = requests.get(self.url).text
        self.html = BeautifulSoup(reg, 'lxml')

    def parsing(self):
        nw = self.html.find_all('div', class_="se-news-list-page__item")
        for item in nw:
            time = item.find('div', class_="se-news-list-page__item-left").text.strip()
            time = time[:5] + ' ' + time[5:]
            news = item.find('div', class_='se-material__title').text.strip()
            href = item.find('div', class_='se-material__title').find('a').get('href')
            self.res.append({
                'time': time,
                'news': news,
                'href': href
            })

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.res:
                f.write(f"Новость № {i}\nВремя: {item['time']}\nНовость: {item['news']}\nСсылка: {item['href']}"
                        f"\n\n{'__' * 30}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
