# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#
#     return s
#
#
# print("Сумма четных чисел: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
#
# print("Сумма нечетных чисел: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))


# lts1 = [1, 2, 3]
# lts2 = [1, 2, 3]
# print(lts1 == lts2)
# print(lts1 is lts2)
# print(id(lts1))
# print(id(lts2))
#
# a = 3
# b = 3
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))


# def add_number(n):
#     print("n1", n, "=", id(n))
#     n += 1
#     print("n2", n, "=", id(n))
#
#
# x = 1
# print("x1", x, "=", id(x))
# add_number(x)
# print("x2", x, "=", id(x))


# ..................Кортеж(tuple)..............................


# lts = [1, 2, 3]
# tpl = (1, 2, 3)
# print(lts.__sizeof__())
# print(tpl.__sizeof__())
# print(type(tpl))


# tpl = (1, 2, 3, 4, 5, 6, 7)
# print(tpl)
# print(tpl[2])

# from random import randint
# # s = tuple([input("->") for i in range(3)])
# s = tuple(randint(1, 30) for i in range(3))
# print(s)


# tpl = tuple(2 ** i for i in range(1, 12))
# print(tpl)


# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(t3.count('l'))


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 8, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
