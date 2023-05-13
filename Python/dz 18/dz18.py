# .................Задача № 1....................

# with open("dz18.txt", 'w') as f:
#     f.write("Замена строки в текстовом файле;\nИзменить строку в списке;\nЗаписать список в файл;\n")
#
# pos1 = int(input("pos1 = "))
# pos2 = int(input("pos2 = "))
#
# with open("dz18.txt", "r") as f:
#     lines = f.readlines()
#     if pos1 - 1 >= len(lines) or pos2 - 1 >= len(lines):
#         print("Ошибка, повторите попытку")
#     else:
#         lines[pos1 - 1], lines[pos2 - 1] = lines[pos2 - 1], lines[pos1 - 1]
# with open("dz18.txt", "w") as f:
#     f.writelines(lines)
# print(lines)


# .................Задача № 2....................

# with open("dz18_two.txt", 'w') as f:
#     f.write("Замена строки в текстовом файле;\nИзменить строку в списке;\nЗаписать список в файл\n;")
#
# with open("dz18_two.txt", 'r') as f:
#     lines = f.readlines()
#     lines = lines[::-1]
#
# with open("dz18_two.txt", 'w') as f:
#     f.writelines(lines)
#
# print(lines)
