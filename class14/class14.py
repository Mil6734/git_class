# ....................Декораторы.......................

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello()
# print(test)


# def my_decorator(func):  # декорирующая функция
#     def func_wrapper():
#         print('Код до функции')
#         func()
#         print('Код после функции функции')
#
#     return func_wrapper
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("тело функции 'func_test'")
#
#
# func_test()
# # test = my_decorator(func_test)
# # test()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return 'text'
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print(arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(name, surname):
#     print("Меня зовут", name, surname)
#
#
# print_full_name("Андрей", "Жирнов")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args:', args)
#         print('kwargs:', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Андрей", "Жирнов", "Света", study="JavaScript")
# print_full_name("Влад", "Игорь", "Женя")


# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# print(int('19'))
# print(int('19.5'))  # ValueError


# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))


# print(bin(18))  # 0b10010 десятеричная системы счисления
# print(oct(18))  # 0o22 восьмеричная система счисления
# print(hex(18))  # 0x12 шестнадцатеричная система счисления


# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print("P" in e)


# s = "Hello"
# print(s[1])
# print(s[-5])
# print(s[1:4])
# print(s[::-1])


# s = 'python'  # pytton
# # s[3] = 't'  # ошибка
# s = s[:3] + 't' + s[4:]
# print(s)


# def change_to_str(s, c_old, c_now):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_now
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = change_to_str(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)


# print("Привет")
# print(u"Привет")


print("C:\\folder\\file.txt")
print(r"C:\folder\file.txt")