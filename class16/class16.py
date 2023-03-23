#  ...........................Регулярные выражения.......................
# import re
#
# s = 'Я ищу совпадения в 2023 году. И я их найду в два счёта.'
# ref = 'в'
# print(re.findall(ref, s))  # возвращает список, содержащий все совпадения с шаблоном
# print(re.search(ref, s))   # местоположение первого совпадения объекта
# print(re.search(ref, s).span())
# print(re.search(ref, s).start())
# print(re.search(ref, s).end())
# print(re.search(ref, s).group())
# print(re.match(ref, s))  # местоположение совподений объекта в начале строки
# print(re.split(ref, s))
# print(re.sub(ref, 'Я', s))  # поиск и замена
# print(re.sub(ref, 'Я', s, 3))  # количество заменяемых элементов
# print(re.split(ref, s, 2))  # возвращает список в котором строка разбита по шаблону
import re


# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9683'
# # ref = '[12][0-9][0-9][0-9]'
# # ref = '[А-Яа-яё]'
# # ref = '.'  # каждый любой символ
# ref = r'[^0-9]'  # все кроме заданного диапазона
# print(re.findall(ref, s))


# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9683'
# reg = r'\w+'
# print(re.findall(reg, s))


# d = 'Цифры: 7, +17, -42, 0012, 0.3'
# print(re.findall(r"[+-]?\d+[.\d]*", d))


# s = '06-03-1987 # Дата рождения'
# print('Дата рождения', re.sub(r'#.*', '', s))
# print('Дата рождения', re.sub(r'-', '.', re.sub(r'#.*', '', s)))


# s = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# # reg = r'\w+\s*=\s*\w+[\s\w.]*'
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, s))


# s = '12 сентября 2021 года'
# reg = r'\d{2,4}'
# print(re.findall(reg, s))


# s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s))


# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9683'
# # reg = r'^\w+\s\w+'
# print(re.findall(reg, s))


def validate_login(name):
    return re.findall(r'^[A-Za-z_0-9-]{3,16}$', name)


print(validate_login("Python_master"))
print(validate_login("pyt09#h"))


# print(re.findall(r'\w+', '10 + й'))
