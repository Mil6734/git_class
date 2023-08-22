# CSV (Comma Separated Values - переменные, разделенные запятые)

import csv


# with open('data.csv', encoding='utf8') as f:
#     file_reader = csv.reader(f, delimiter=';')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"File {', '.join(row)}")
#         else:
#             print(f"\t\t{row[0]} - {row[1]}")
#         count += 1


# with open('data2.csv') as f:
#     file_reader = csv.reader(f, delimiter=';')
#     for row in file_reader:
#         print(row)


# with open('data.csv', encoding='utf8') as f:
#     file_reader = csv.DictReader(f, delimiter=';')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"File {', '.join(row)}")
#         print(f"\t\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году.")
#         count += 1


# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['Имя', "Класс", "Возраст"])
#     writer.writerow(['Женя', "9", "15"])
#     writer.writerow(['Саша', "8", "14"])
#     writer.writerow(['Маша', "11", "18"])


data = [['hostname', 'vendor', 'model', 'location'],
        ['sw1', 'Cisco', '3750', 'London, Best str'],
        ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
        ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
        ['sw4', 'Cisco', '3650', 'London, Best str']]


with open('data_new.csv', 'w') as f:
    writer = csv.writer(f, delimiter=';', lineterminator='\r')
    for row in data:
        writer.writerow(row)


# with open('student1.csv', 'w') as f:
#     names = ["Name", "Age"]
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Name": "Andrey", "Age": "22"})
#     writer.writerow({"Name": "Alexey", "Age": "32"})
#     writer.writerow({"Name": "Natalya", "Age": "55"})


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict_writer.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
#
# with open('todos.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(todos[0].keys()))
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)


# import requests
# pip install beautifulsoup4 или bs4
from bs4 import BeautifulSoup
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# # row = soup.find("div", class_="name").text
# # row = soup.find_all("div", class_="name")
# # row = soup.find_all("div", class_="row")[1].find('div', id='whois1')
# # row = soup.find("div", string="Alena").parent
# # row = soup.find("div", string="Alena").find_parent("div", class_='row')
# # row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
#
# print(row)


# def get_copy(tag):
#     whois = tag.find('div', class_='whois')
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all("div", class_="row")
# copy = []
# for i in row:
#     cw = get_copy(i)
#     if cw:
#         copy.append(cw)
#
# print(copy)


import re


def get_salary(s):
    pattern = r"\d+"
    # res = re.findall(pattern, s)
    res = re.search(pattern, s).group()
    print(res)


f = open('index.html', encoding='utf-8').read()
soup = BeautifulSoup(f, 'html.parser')
row = soup.find_all("div", {"data-set": "salary"})
for i in row:
    get_salary(i.text)






