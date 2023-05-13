# Модули OS и OS.PATH

import os
import os.path


# print("Текущая директория:", os.getcwd())  # C:\pythonMy\myProject\git_class\class19
# print(os.listdir())  # возвращает имена файлов и папок из текущей директории
# print(os.listdir(".."))  # На уровень выше
# os.mkdir("folder")  # создание папки
# os.makedirs("nested1/nested2/nested3")  # создание папки и всех папок
# os.rmdir("folder")  # удаление пустой директории
# os.remove("xyz.txt")  # удаляет файл
# os.rename('gjk.txt', 'new.txt')  # переименовывает файл или папки
# os.rename('new.txt', 'nested1/two.txt')  # переносит файл или папку в другую директорию
# os.renames('gg.txt', 'gg/gg_new.txt')  # создает промежуточные директории

# for root, dirs, files in os.walk("nested1"):
#     print('Root:', root)
#     print('Subdirs:', dirs)
#     print('Files:', files)


# def remove_empty_dirs(root_three):
#     print(f"Удаление пустых директорий в ветке {root_three}")
#     print("-" * 50)
#     for root, dirs, files in os.walk("nested1", topdown=False):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print("-" * 50)
#
#
# remove_empty_dirs("nested1")


# print(os.path.split(r"C:\pythonMy\myProject\git_class\class19\nested1\two.txt"))  # разбивает путь на кортеж(head,tail
# # tail - последний компонент пути, head - остальная часть
#
# print(os.path.dirname(r"C:\pythonMy\myProject\git_class\class19\nested1\two.txt"))  # путь до последнего элемента
# print(os.path.basename(r"C:\pythonMy\myProject\git_class\class19\nested1\two.txt"))  # последний компонент пути


# print(os.path.join('C:\pythonMy', 'myProject', 'git_class', 'class19', 'two.txt'))


# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, 'w').close()
#
# files_width_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in files_width_text:
#     with open(file, 'w') as f:
#         f.write(f'Некоторый текс для документа {file}')
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, fl in os.walk(root, topdown):
# #         print(root)
# #         print(dirs)
# #         print(fl)
# #     print('-' * 50)
#
# print_tree('Work', False)
# print_tree('Work', True)


# print(os.path.exists(r"C:\pythonMy\myProject\git_class\class19\nested1\two.txt"))  # Возвращает True если путь верен

# import time
#
# path = r'C:\pythonMy\myProject\git_class\class19\class19.py'
# print(os.path.getsize(path))  # размер файла в байтах
# print(os.path.getmtime(path))  # Возвращает время последнего изменения файла
# print(os.path.getatime(path))  # Возвращает время последнего доступа к файлу
# print(os.path.getctime(path))  # Возвращает время создания файла
#
# a_time = os.path.getmtime(path)
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a_time)))
#
# print(os.path.isdir(r'C:\pythonMy\myProject\git_class\class19\class19.py'))  # Возвращает True если путь явл папкой
# print(os.path.isfile(r'C:\pythonMy\myProject\git_class\class19\class19.py'))  # Возвращает True если путь явл файлом


# file_path = r'nested1\nested2\nested3\nt3.txt'
# if os.path.exists(file_path):
#     d, name = os.path.split(file_path)
#     print(f"{name} ({d}), -last access time {os.path.getmtime(file_path)} sec")
# else:
#     print("File is not exist")


# class Point:
#     """Класс для предоставления координат точки плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# Point.x = 100
# p1.x = 30
# print(p1.x)
# print(p1.__dict__)
#
# # p2 = Point()
# # print(p2.x)


class Point:
    x = 1
    y = 1

    def set_coord(self):
        print(self.__dict__)


p1 = Point()
p1.x = 5
p1.y = 10
p1.set_coord()
# Point.set_coord(p1)
