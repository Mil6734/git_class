# import requests
#
# res = requests.get("https://ru.wordpress.org/")
# res.encoding = 'utf-8'
# # print(res.headers)
# # print(res.content)
# print(res.text)


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find('p', class_="site-title").text
#     print(p1)
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refined(s):
#     return re.sub(r'\D+', '', s)
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['rating'
#                                                          '']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all('section', class_="plugin-section")[3]
#     plugins = p1.find_all('article')
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         url = plugin.find('h3').find('a').get('href')  # ["href"]
#         rating = plugin.find('span', class_='rating-count').find('a').text
#         r = refined(rating)
#
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import csv
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open('plugins1.csv', 'a') as f:
#         writer = csv.writer(f, delimiter=';', lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all('article', class_='plugin-card')
#     for el in p1:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#         print(name)
#
#         try:
#             url = el.find('h3').find('a')['href']
#         except ValueError:
#             url = ''
#         # print(url)
#
#         try:
#             snippet = el.find("div", class_='entry-excerpt').text
#         except ValueError:
#             snippet = ''
#         # print(snippet)
#
#         try:
#             active = el.find('span', class_='active-installs').text.strip()
#         except ValueError:
#             active = ''
#         # print(active)
#
#         try:
#             c = el.find('span', class_='tested-with').text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ''
#         # print(cy)
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(2, 5):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


from parsers import Parser


def main():
    pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
    pars.run()


if __name__ == '__main__':
    main()
