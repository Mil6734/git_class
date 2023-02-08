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

from random import randint


# def zna(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# a = [randint(1, 20) for i in range(0, 10)]
#
# print(a)


def zna(lts):
    return lts


x = zna([randint(1, 20) for i in range(0, 10)])
print(x)
print(min(x))
