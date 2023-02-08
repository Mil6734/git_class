# import math
#
# num = math.sqrt(4)
# num2 = math.ceil(3.2)
# num3 = math.pi
# print(num)
# print(num2)
# print(num3)

# import math
# a = int(input("Радиус окружности"))
# s = round(2 * math.pi * a, 2)
# print("Длинна окружности", s)


# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
#
# s = time.time()
# print(s)
#
# local = time.ctime(3011200067)
# print(local)
#
# res = time.localtime()
# print(res)
#
# print(time.strftime("%B %d (%A), %Y."))


# pause = 5
# print("Запущена")
# time.sleep(pause)
# print("Закончена")


# import time
# text = input("Название напоминания: ")
# t = float(input("Введите сколько минут"))
# t = t * 60
# time.sleep(t)
# print(text, "?")


# import time
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# print()
#
#
# def hello(name):
#     print("hello", name)
#
#
# hello("Andrey")


# def get_summ(a, b):
#     print("Сумма")
#     return a + b
#
#
# res = get_summ(2, 5)
# print(res)


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def cub(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе", cub(i))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(10, 5))
# print(func(10, 15))


def check_password(password):
    has_upper = False

    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True

    if len(password) >= 8 and has_upper:
        return True
    return False


p = input("Введите пароль: ")
if check_password(p):
    print("Это надежный пароль")
else:
    print("Это не надежный пароль")
