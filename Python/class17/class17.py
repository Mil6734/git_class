import re


# text = "<body>Пример жадного соответствия регулярного выражения</body>"
# print(re.findall('<.*?>', text))

# s = "<p>Изображение <img alt='картинка' src='gg.jpg' width='200'> - фон страницы"
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'  # правильный шаблон для поиска
# print(re.findall(reg, s))

# s = 'Петр, Ольга и Виталий отлично учатся!'
# reg = 'Петр|Ольга|Виталий'  # или одно, или другое
# print(re.findall(reg, s))


# s = 'int = 4, float = 4.0, double = 8.0f'
# # # reg = r'\w+\s*=\s*\d[.\w]*'
# # reg = r'int\s*=\s*\d[.\w]*|double\s*=\s*\d[.\w]*'
# reg = r'(?:int|double)\s*=\s*\d[.\w]*'
# print(re.findall(reg, s))

#  () - сохраняющие скобки
#  (?:) - не сохраняющие скобки


# s = "Word2016, PS6, AI5"
# reg = r'([a-z]+\d*)'
# print(re.findall(reg, s, re.IGNORECASE))

#
# text = '''
# Самара
# Москва
# Тверь
# Уфа
# '''
# count = 0
#
#
# def repl_count(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print("<select>")
# print(re.sub(r'\s*(\w+)\s*', repl_count, text))
# print("</select>")


# s = "Самолет прилетает 10/23/2021. Будем рады вас видеть после 10/24/2021"
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))


# s = "yandex.ru and yandex.com"
# reg = r'(([a-z0-9\-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))


# ..............................Рекурсия....................................

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("на каком вы этаже "))
# elevator(n1)


# def sum_list(lts):
#     res = 0
#     for i in lts:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lts):  # [1, 3, 5, 7, 9] по очереди удаляет элементы
#     if len(lts) == 1:
#         return lts[0]
#     else:
#         return lts[0] + sum_list(lts[1:])  # 1 + 3 + 5 + 7 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))


names = ["Adam", ["Bob", ["Chet", ["Cat"]], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))


def count_items(items_list):
    count = 0
    for item in items_list:
        if isinstance(item, list):
            count += count_items(item)
        else:
            count += 1
    return count


print(count_items(names))