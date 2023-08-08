# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Не верный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым  положительным числом")
#         if key >+ len(self.marks):
#             off = key + 1 - len(self.marks)  # off = 10 + 1 - 5 = 6
#             self.marks.extend([None] * off)  # [5, 5, 3, 4, 5, None, None, None, None, None, None]
#         self.marks[key] = value  # [5, 5, 3, 4, 5, None, None, None, None, None, 6]
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Виктор", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)


# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{self.get_form(h)}:{self.get_form(m)}:{self.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         return self.sec == other.sec
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == 'hour':
#             return (self.sec // 3600) % 24
#         elif item == 'min':
#             return (self.sec // 60) % 60
#         elif item == 'sec':
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == 'hour':
#             self.sec = s + 60 * m + value * 3600
#         elif key == 'min':
#             self.sec = s + 60 * value + h * 3600
#         elif key == 'sec':
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# print(c1['hour'], c1['min'], c1['sec'])
#
# c1['hour'] = 9
# c1['min'] = 3
# c1['sec'] = 8
# print(c1['hour'], c1['min'], c1['sec'])
# print(c1.get_format_time())


# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f'{self.name} is good boy!!!'
#         elif self.pol == 'F':
#             return f'{self.name} is good girl'
#         else:
#             return f'{self.name} is good Kitty'
#
#     def __repr__(self):
#         return f"Cat(name ='{self.name}', age = '{self.age}', pol = '{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(['M', 'F'])) for _ in range(randint(1, 5))]
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat('Tom', 4, 'M')
# cat2 = Cat('Else', 5, "F")
# # cat3 = Cat('Murzik', 5, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)


#  ................................полиморфизм


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
# for g in shape:
#     print(g.get_perimetr())


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)  # 10 + 35
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))  # len('10') + str(35) = len('1035') => 4
#
#
# t1 = Number(10)
# t2 = Text('10')
#
# print(t1.total(35))
# print(t2.total(35))


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}')
#
#     def make_sound(self):
#         return f'{self.name} мяукает'
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(f'Я собака. Меня зовут {self.name}. Мой возраст {self.age}')
#
#     def make_sound(self):
#         return f'{self.name} гавкает'
#
#
# a = [Cat('Пушок', 2.5), Dog('Мухтар', 4)]
#
# for i in a:
#     i.print_info()
#     print(i.make_sound())


# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'\n{self.surname} {self.name} {self.age}', end=" ")
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, speciality, groups, rating):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.group = groups
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f'{self.speciality} {self.group} {self.rating}', end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, speciality, experience):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f'{self.speciality} {self.experience}', end=" ")
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, speciality, groups, rating, topic):
#         super().__init__(surname, name, age, speciality, groups, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f'{self.topic}', end=" ")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()


#  ...................................Функторы................................

# def func():
#     def wrap():
#         return "Hello"
#
#     return wrap
#
#
# a = func()
# print(a())


class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(self.count)


c1 = Counter()
c1()