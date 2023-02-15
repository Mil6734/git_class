# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append('hi')
# print(t, id(t))


# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # Распаковка кортежа
# print(x, y, z)


# def get_user():
#     name = "tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name, year, married)


# lts = [1, 2, 3, 4, 5]
# print(type(lts))
# print(lts)
# tpl = tuple(lts)
# print(type(tpl))
# print(tpl)


# countries = (
#     ("Германия", 80.2, (("Берлин", 3.236), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.6), ("Марсель", 1.6)))
# )
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "\nНаселение страны:", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, "(Население: ", city_population, ")", sep="")


#   ..........................Множество(set)................................

# s = {"banana", "apple", "orange", "apple", "orange"}
# print(s)
# print(type(s))

# a = {}
# print(type(a))
# print(a)


# def to_set(a):
#     x = set(a)
#     n = len(x)
#     return x, n
#
#
# print(to_set('я обычный текст'))
# print(to_set([4, 5, 6, 4, 9, 11, 3, 4, 2]))


# t = {'red', 'green', 'blue'}
# print('green1' not in t)
# for i in t:
#     print(i)


# lts = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in lts if 'a' in i}
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lts if i[1] == 'c'] # Коротки вариант записи
# print(a)
#
# for i in lts:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])


# users = {"tom", "alice", "bob"}
# users.add('loli')
# print(users)
# users.remove('bob')
# print(users)
# users.pop()     # Удаляет первый элемент множества
# print(users)
# users.clear()   # Полное очищение множества
# print(users)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # c = a & b
# # c = a - b
# c = a ^ b
# print(c)
#
# # a |= b
# # print(a)


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))


# a = set(input("Первая строка: "))
# b = set(input("Вторая строка: "))
# c = a & b
# print(c)


# ...................Словарь(dict)......................

# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# d1 = dict(one=1, two=2)
# print(d1)

# lts = ["one", "two", "three"]
# print(dict(lts))  # Преобразить в словарь нельзя

a = [
    ('one', 1),
    ('two', 2),
    ('three', 3)
]

print(dict(a))
