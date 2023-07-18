# class Figur:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figur):
#     def __init__(self, width, height, color):
#         self.__width = width
#         self.__height = height
#         super().__init__(color)
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительным числом")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота должна быть положительным числом")
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника {self.__width}x{self.__height}:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.width)
# print(rect.height)
# print(rect.color)
# print(rect.area())
# print(rect.__dict__)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#
# line = Line(Point(1, 2), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(5, 14), Point(30, 54))
# line.draw_line()
# print()
# rect = Rect(Point(10, 20), Point(200, 300))
# rect.draw_rect()
# rect.set_coord(Point(5, 14), Point(30, 54))
# rect.draw_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник: \nШирина {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Фон: {self.fon}")
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         self.border = border
#         super().__init__(width, height)
#
#     def show_border(self):
#         super().show_rect()
#         print(f"Рамка: {self.border}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 200, "1px solid red")
# shape2.show_border()


# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))


# Перегрузка методов(в чистом виде его нет)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#     def set_coord(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print(" Первая координата должны быть целыми числами")
#
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целыми числами")
#
#
# rect = Rect(Point(1, 2), Point(10, 20))
# rect.draw_rect()
# rect.set_coord(Point(10, 30), Point(40, 70))
# rect.draw_rect()
# rect.set_coord(Point(-10, -20))
# rect.draw_rect()


# Абстрактные методы(методы которые написаны в родительском классе)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Ellipse(Prop):
#     # def draw(self):
#     #     print(f'Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}')
#     pass
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
#
# for f in figs:
#     f.draw()


# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):  # Абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):  # Абстрактный метод
#         pass
#
#
# class Queen(Chess):
#     def move(self):
#         print("Ферзь перемещен на е2е4")
#
#
# q = Queen()
# q.draw()
# q.move()


from math import pi


class Table:
    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            self._width = width
            self._length = length
        else:
            self._radius = radius

    def calc_area(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")


class SqTable(Table):
    def calc_area(self):
        return self._width * self._length


class RoundTable(Table):
    def calc_area(self):
        return round(pi * self._radius ** 2, 2)


t = SqTable(20, 10)
print(t.__dict__)
print(t.calc_area())
t1 = RoundTable(radius=20)
print(t1.__dict__)
print(t1.calc_area())
