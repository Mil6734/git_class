# ................Замыкание...................

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
# add2 = outer(6)
# print(add2(11))
#
# print(outer(5)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + '_new'
#         return a, b, c
#
# #     return func2
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def incr():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return incr
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res1()


# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 35,
#     'Grace': 69
# }
#
#
# def make(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = make(80, 100)
# B = make(70, 80)
# C = make(50, 70)
# D = make(0, 50)
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))


# ......................Анонимные функции(lambda)..................


# print((lambda x, y: x + y)(1, 2))
# (lambda x, y: print(x + y))(1, 3)

# func = lambda x, y: x + y
# print(func(1, 2))

# print((lambda x=2, y=5: x + y)())


# c = (lambda x: x * 2, lambda x: x * 3, lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))


# print("summ3 =", (lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))


# d = {'d': 10, 'b': 15, 'c': 4}
# # a = sorted(d)  # сортировка по ключам
# # print(a)
#
# list_d = list(d.items())
# list_d.sort(key=lambda i: i[1])  # сортировка по значению
# print(list_d)


# a = {'one': lambda x: x - 1, 'two': lambda x: x * (-1), 'three': lambda x: x ** 5}
# b = [-3, 10, 0, 4]
# for i in b:
#     if i < 0:
#         print(a['two'](i))


# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда")
#
# }
#
# d[2]()


# print((lambda a, b: a if a > b else b)(5, 3))


# ........map(func, iterables), filter(func, iterables)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# a = list(map(mult, lst))
# print(a)
#
# a1 = list(map(lambda t: t * 2, lst))
# print(a1)


