#  ........................Декораторы....................

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('перед вызовом функции')
#         self.func()
#         print('после вызова функции')
#
#
# @MyDecorator
# def hello():
#     print("Hello")
#
#
# hello()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = 'перед вызовом функции\n'
#         res += str(self.func(a, b))
#         res += '\n после вызова функции'
#         return res
#
#
# @MyDecorator
# def hello(a, b):
#     return a * b
#
#
# print(hello(2, 5))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def result(a, b):
#     return a * b
#
#
# print(result(2, 3))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         res = 'перед вызовом функции\n'
#         res += str(self.func(*args, **kwargs))
#         res += '\nпосле вызова функции'
#         return res
#
#
# @MyDecorator
# def hello(a, b):
#     return a * b
#
#
# @MyDecorator
# def hello1(a, b, c):
#     return a * b * c
#
#
# print(hello(2, 5))
# print(hello1(2, 5, 2))


# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(*args, **kwargs):
#             res = 'перед вызовом функции\n'
#             res += self.arg + str(func(*args, **kwargs))
#             res += '\nпосле вызова функции'
#             return res
#
#         return wrap
#
#
# @MyDecorator("Результат умножения:")
# def hello(a, b):
#     return a * b
#
#
# print(hello(2, 5))


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             return func(a, b) ** self.arg
#
#         return wrap
#
#
# @Power(3)
# def result(a, b):
#     return a * b
#
#
# print("Результат:", result(2, 2))


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("(*)" * 10)
#         fn(*args, **kwargs)
#         print("(*)" * 10)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person("Андрей", "Андреев")
# p1.info()


# def decorator(cls):
#     class Wrapper(cls):
#         def method_2(self, value):
#             print("cls = ", cls)
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def method_1(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.method_1(4))
# print(obj.method_2(4))


#  ...............................Дескрипторы..................


# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{value} должно быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person("Андрей", "Андреев")
# p.name.set("Алексей")
# print(p.name.get())


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Андрей", "Андреев")
# p.name = "Алексей"
# print(p.name)
# print(p.surname)


# class NonNegative:
#     def  __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Значение должно быть положительным")
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())


# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата {coord} должна быть целым числом ")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# p1.z = 6
# print(p1.z)
# print(p1.__dict__)


# ......................... Создание модулей .........................


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimetr(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_perimetr(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimetr(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)
shape = [r1, r2, s1, s2, t1, t2]
for g in shape:
    print(g.get_perimetr())
