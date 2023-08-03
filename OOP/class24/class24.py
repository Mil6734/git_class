# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# elem = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
#
# for d in elem:
#     d.print_value()
#     print(f"= {d.convert_to_rub():.2f} RUB")
# print(50 * "*")
#
# elem1 = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# for i in elem1:
#     i.print_value()
#     print(f"= {i.convert_to_rub():.2f} RUB")


# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# def func():
#     x = 2
#
#     def inner():
#         n = 4
#         return n + x
#
#     return inner()
#
#
# print(func())
# print(x)


# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("outer_class_method")
#
#     def outer_obj_method(self):
#         print("outer_obj_method")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("inner_method", MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# print(out.name)
# inner = out.MyInner("внутренний", out)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()


# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.inter = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#
#         def display(self):
#             print("Name:", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Alba"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Employee()
# outer.show()
# d1 = outer.inter
# d1.display()
# d2 = outer.head
# d2.display()


# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Внешний класс")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Вложенный класс")
#
#         class InnerClass:
#             def show(self):
#                 print("Класс внутри вложенного класса")
#
#
# outer = Outer()
# outer.show()
#
# # inner1 = outer.inner
# # inner1.show()
#
# # inner2 = inner1.inner_inner
# inner2 = outer.inner.inner_inner
# inner2.show()


# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("Базовый класс")
#
#     class Inner:
#         def display1(self):
#             print("Вложенный класс внутри базового")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("Дочерний класс")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Вложенный класс внутри дочернего')
#
#
# a = SubClass()
# a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5, 9, 4)
# print(len(p))


# class Point:
#     __slots__ = ('x', 'y', 'z')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p1.z = 20
# # print(p1.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p2 = Point2(5, 10)
# print("p1 =", p1.__sizeof__())
# print("p2 =", p2.__sizeof__() + p2.__dict__.__sizeof__())


class Creature:
    def __init__(self, name):
        self.name = name


class Animal(Creature):
    def sleep(self):
        print(self.name, "is sleeping")


class Pet(Creature):
    def play(self):
        print(self.name, "is playing")


class Dog(Animal, Pet):
    def bark(self):
        print(self.name, "is barking")


b = Dog("Buddy")
b.bark()
b.play()