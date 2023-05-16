# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
#
#
# p2 = Point()
# # p2.x = 20
# # p2.y = 40
# p2.set_coord(20, 40)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, '*'))
#         print(f"Имя:{self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}"
#               f"\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_city(self, city, phone, address):  # установить
#         self.city = city
#         self.phone = phone
#         self.address = address
#
#     def get_all(self):  # получить
#         return self.city, self.phone, self.address
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_city("Саратов", "64-68-07", "Тухачевского 8")
# h1.print_info()
# print(h1.get_all())


# class Person:
#     skill = 10  # статическое свойство
#
#     def __init__(self, name, surname):
#         self.name = name  # динамическое свойство
#         self.surname = surname  # динамическое свойство
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p2.add_skill(2)
#
# # свойства бывают 2 типов(статические и динамические)
# # Специальные (магическое) методы - конструктор(__new__), инициализатор(__init__), деструктор(__del__)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляров")
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# # del p1
# p1 = 0
# print(p1.x)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         if isinstance(x, int) and isinstance(y, int):
#             self.x = x
#             self.y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.x, self.y
#
#
# p1 = Point(5, 10)
# p1.set_coord("12", "aaa")
# print(p1.get_coord())


# class Point:
#     count = 0
#
#     def __init__(self, x=1, y=1):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point()
# print("p1 = ", p1.count)
# p2 = Point()
# print("p2 = ", p2.count)
# p3 = Point()
# print("p3 = ", p3.count)
# print("Point = ", Point.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последний")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов", Robot.k)
#
# print()
#
# droid2 = Robot('C-3DO')
# droid2.say_hi()
# print("Численность роботов", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.\n")
#
# del droid1
# del droid2
#
# print("Численность роботов", Robot.k)


# Модификаторы доступа: public(self.x), protected(self._x), private(self.__x)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# p1.set_coord(80.2, 120)
# print(p1.get_coord())
# print(p1.__dict__)