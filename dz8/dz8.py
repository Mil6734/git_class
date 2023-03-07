# Задача 1

# from math import pi
#
#
# def figure(x):
#     if x == 1:
#         a = int(input("Длина: "))
#         b = int(input("Ширина "))
#         return a * b
#     elif x == 2:
#         a = int(input("Основание: "))
#         b = int(input("Высота "))
#         return (a * b) / 2
#
#     elif x == 3:
#         a = int(input("Радиус: "))
#         return 2 * pi * a
#
#
# col = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
# print("Площадь", figure(col))


# Задача 2

# from random import randint


# def zna(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# x = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
# a = zna(x)
#
# print(a)
#
# # def zna(lts):
# #     return lts
# #
#
# x = zna([6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1])
# print(x)


def fn(lts):
    v = min(lts)
    return v


s = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
print(s)
fn(s)


данн список целых чисел. Найти минимальное среди простых чисел и максимальное среди чисел не являющихся простыми