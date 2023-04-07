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

s = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]


def check(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_num = [num for num in s if check(num)]
non_prime = [num for num in s if not check(num)]

min_num = min(prime_num)
max_num = max(non_prime)

print("Min: ", min_num)
print("Max: ", max_num)
