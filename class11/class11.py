# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)


# d = {i: input("->") for i in range(1, 5)}
# print(d)
# des = int(input("Какой ключ удалить"))
# del d[des]
# print(d)


# goods = {
#     '1': ['Core-i3-4300', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['Amd FX-43600', 6, 3700],
#     '4': ['Pentium 63220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
#
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "rub", sep="")
#
# while True:
#     n = input("№: ")
#     if n != '0':
#         qty = int(input("Количество "))
#         goods[n][1] = qty
#     else:
#         break
#
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "rub", sep="")


# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d
# print("D = ", d)
# print("D2 = ", d2)


# d = {'a': 1, 'b': 2, 'c': 3}
# value = d.get('b1', 'нет такого ключа')
# print(value)
# print(d.keys())     # ключи
# print(d.values())   # значения
# print(d.items())    # ключ + значения
# item = d.pop('b')   # удаляет по ключу
# item = d.popitem()  # удаляет последний ключ и значение
# item = d.setdefault('e', 100)   # устанавливает значение по умолчанию
# d.update([('r', 7), ('x', 8)])
# d.update({'r': 7, 'x': 8})
#
# print(item)
# print(d)


# .........................zip()........................

a = [1, 2, 3]
b = ['Dec', 'Jan', 'Feb']
d = dict(zip(a, b))
print(d)
