# class Rectangle:
#
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_width(self, w):
#         if Rectangle.__check_value(w):
#             self.__width = w
#
#     def set_length(self, lg):
#         if Rectangle.__check_value(lg):
#             self.__length = lg
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__width * self.__length
#
#     def get_draw(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# a = Rectangle()
# a.set_length(3)
# a.set_width(9)
# print("Длинна прямоугольника:", a.get_length())
# print("Ширина прямоугольника:", a.get_width())
# print("Площадь прямоугольника:", a.get_area())
# # print(a.__dict__)
# a.get_draw()


# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# # print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print("__set_x")
#         self.__x = x
#
#     def __get_x(self):
#         print("__get_x")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# # p1.__set_x(45)
# p1.x = 45
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         print("__get_x")
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         print("__set_x")
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#
# p1 = Point(5, 10)
# # p1.__set_x(45)
# p1.x = 45
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (float, int)):
#             self.__kg = new_kg
#         else:
#             raise TypeError("Килограммы задаются только числами")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pound(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pound(), "фунтов")
# weight.kg = 'десять'


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def x(self):
#         return self.__name
#
#     @x.setter
#     def x(self, name):
#         self.__name = name
#
#     @x.deleter
#     def x(self):
#         del self.__name
#
#     @property
#     def y(self):
#         return self.__age
#
#     @y.setter
#     def y(self,age):
#         self.__age = age
#
#     @y.deleter
#     def y(self):
#         del self.__age
#
#
# pep = Person("Irina", 31)
# print(pep.__dict__)
# pep.x = "Igor"
# pep.y = 26
# print(pep.x)
# print(pep.y)
# print(pep.__dict__)
# del pep.x
# print(pep.__dict__)


# методы (функции) - статические() @staticmethod, класса(cls) @classmethod, экземпляра класса(self)

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# print(p1.get_count())
# p2 = Point()
# print(p2.get_count())
# p3 = Point()
# print(p3.get_count())
# print(Point.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))


# import math
#
#
# class Area:
#     __count = 0
#
#     @staticmethod
#     def triangle_area_1(a, b, c):
#         Area.__count += 1
#         p = (a + b + c) / 2
#         return math.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area_2(a, h):
#         Area.__count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.__count += 1
#         return a ** 2
#
#     @staticmethod
#     def rect_area(a, b):
#         Area.__count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.__count
#
#
# print(f"Площадь треугольника по формуле Герона: {Area.triangle_area_1(3, 4, 5)}")
# print(f"Площадь треугольника через основание и высоту: {Area.triangle_area_2(6, 7)}")
# print(f"Площадь треугольника: {Area.square_area(7)}")
# print(f"Площадь прямоугольника: {Area.rect_area(2, 6)}")
# print(f"Количество вызовов: {Area.get_count()}")


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, string_date):
        day, month, year = (map(int, string_date.split('.')))
        return cls(day, month, year)

    def string_to_db(self):
        return f"{self.year}--{self.month}--{self.day}"


# string_date = '23.10.2022'
# day, month, year = (map(int, string_date.split('.')))
date = Date.from_string("23.10.2023")
print(date.string_to_db())
date2 = Date.from_string("30.11.2000")
print(date2.string_to_db())
