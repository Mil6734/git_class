# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("  Hello\tWorld "))


#  .....................Работа с файлами.................
#   все картинки лежат в папке 19

# f = open(r'C:\pythonMy\myProject\git_class\class18\text.txt')
# f = open('text.txt')  # если файл лежит рядом с проектом
# print(f)
# print(*f)
# print(f.mode)
# print(f.encoding)
# print(f.name)
# f.close()
# print(f.closed)


# f = open('text.txt')
# print(f.read(3)) # считывает количество символов
# print(f.read())
# f.close()


# f = open("test.txt")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()


# f = open("test.txt")
# print(f.readlines(2))
# print(f.readlines())
# f.close()


# f = open("test.txt")
# print(len(f.readlines()))
# f.close()


# f = open("xyz.txt", mode='w')  # w - создает новый файл, а если файл уже существует, то очищает его данные
# f.write("hello")  # write - дает возможность записать строку в текстовый документ
# f.close()


# f = open("xyz.txt", 'a')
# # f.write('New text\n')
# line = ['This in line 1', 'This in line 2']
# f.writelines(line)
# f.close()

# f = open("xyz.txt", 'w')
# lst = [str(i ** 5) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + ' ')
# f.close()


# f = open("text2.txt", 'w')
# f.write("Замена строки в текстовом файле;\nИзменить строку в списке;\nЗаписать список в файл")
# f.close()
#
# f = open("text2.txt", 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = 'Замена\n'
# f.close()
#
# f = open("text2.txt", 'w')
# f.writelines(read_file)
# f.close()


# f = open("text3.txt", 'w')
# f.write("Замена строки в текстовом файле;\nИзменить строку в списке;\nЗаписать список в файл")
# f.close()
#
# i = int(input("pos = "))
#
# f = open("text3.txt", 'r')
# read_file = f.readlines()
# print(read_file)
# if 0 < i <= len(read_file):
#     # read_file[i] = ''
#     del read_file[i]
# else:
#     print("Ошибка")
# f.close()
#
# f = open("text3.txt", 'w')
# f.writelines(read_file)
# f.close()


# f = open("text.txt")
# print(f.read(3))  # Hel
# print(f.tell())  # 3 - возвращает текущую позицию условного курсора в файле
# print(f.seek(1))  # 1 - перемещает курсор в заданную позицию
# print(f.read())  # ello!
# f.close()


# f = open("text.txt", 'a+')
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()


# with open('text.txt', 'w+') as f:
#     print(f.write('01234F56789'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line)


# file_name = 'res.txt'
# lts = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lts))
#
# print('Done!')


# file_name = 'res.txt'
#
#
# with open(file_name, 'r') as f:
#     read_file = f.read().split(" ")
#     print(read_file)
#     print(len(read_file))
#     print(sum(map(float, read_file)))



