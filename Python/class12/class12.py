# a = {'b': 2, 'c': 1, 'a': 4, 'd': 3}
# d = list(a.items())
# print(d)
# n, m = zip(* d)
# print(n)
# print(m)
# c = list(zip(n, m))
# print(c)
# c.sort()
# print(c)
# print(dict(c))
# c = {v: k for k, v in c}
# print(c)


# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Чистая прибыль в", m, "=", profit)


# one = {'a': 1, 'b': 2}
# two = {'c': 3, 'd': 4}
# print({**one, **two})


# data = ['red', 'green', 'blue']
# ind = 1
# for i in data:
#     print(ind, i)
#     ind += 1
# print()
# for n, i in enumerate(data, start=1):
#     print(n, i)


# dict_one = {'name': 'Igor', 'email': 'igor@gmail.com', 'job': 'Consultant'}
#
# for i, (j, v) in enumerate(dict_one.items(), 1):
#     print(i, ')', j, ' - ', v)
# print()
# for i, j in enumerate(dict_one.values(), 1):
#     print(i, ')', ' - ', j)


# def func(*args):
#     return args
#
#
# print(func(5, 3))
# print(func(5, 3, 4))


# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 3, 3))


# def to_dict(*args):
#     return {k: k for k in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))


# def func(*args):
#     a = sum(args) / len(args)
#     print(a)
#     return [x for x in args if x < a]
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(func(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(2))
# print(func(2, 5, 6, 7, 8, 4))


# def print_scores(student, *scores):
#     print("\nStudent Name:", student)
#     # for score in scores:
#     #     print(score, end=" ")
#     print(*scores)
#
#
# print_scores("Jon", 10, 321, 543, 11, 432)
# print_scores("And", 32, 5432, 625, 77)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))


# def intro(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print()
#
#
# intro(name='Irina', surname='Sharma', age=22)
# intro(name='Igor', surname='Wood', age=22, email='igor@gmail.com', phone=94356328840)


# my_dict = {'one': 'first'}
#
#
# # def db(**kwargs):
# #     # global my_dict
# #     # my_dict = my_dict | kwargs
#     # return my_dict
#     my_dict.update(kwargs)
#
#
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print(my_dict)


# def func1(*args):
#     print(args[0])
#
#
# func1(1, 2, 3, 4, 5, 6)


# def func(first, *args, **kwargs):
#     return first, args, kwargs
#
#
# print(func(5, 4, 8, 9, 7, a=6, b=2, c=10))


# .....................Области видимости(scope)..............


# name = "tom"
#
#
# def hi():
#     global name
#     name = 'Sam'
#     surname = "Jon"
#     print("Helo", name, surname)
#
#
# def bye():
#     print("good bye", name)
#
#
# hi()
# bye()
# print()


# x = 3  # третьем берется это значение
#
#
# def and_two(a):
#     # x = 2 # вторым берется это значение
#
#     def add_some():
#         # x = 5 # первым берётся это значение
#         return a + x
#
#     return add_some()
#
#
# print(and_two(3))


# def outer_fuc(who):
#     def inner_func():
#         print("Hello world", who)
#
#     inner_func()
#
#
# outer_fuc("World!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Summa", a + b)
#
#     print('a =', a)
#     fun2(4)
#
#
# fun1


x = 25
t = 0


def fn():
    global t
    a = 30

    def inner():
        nonlocal a
        a = 35

    inner()
    t = a


fn()
z = x + t
print(z)
