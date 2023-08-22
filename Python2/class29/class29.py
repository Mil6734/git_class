# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # a = ''
#         # for i in self.marks:
#         #     a += str(i) + ', '
#         # return f'Студент: {self.name} - {a[:-2]}'
#         a = ', '.join(map(str, self.marks))
#         return f'Студент: {self.name} - {a}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def del_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 1)
#
#     def dump_json(self, file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = []
#
#         data.append({'name': self.name, 'marks': self.marks})
#         with open(file_name, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = '\n'.join(map(str, self.students))
#         return f"Группа {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     def dump_group(self, file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = []
#
#         with open(file_name, 'w') as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def upload_journal(file_name):
#         with open(file_name) as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birk', [3, 5, 3, 2, 5, 4])
# # file1 = 'student_list.json'
# # st3.dump_json(file1)
# # Student.load_from_file(file1)
#
#
# # print(st1)
# #
# # st1.add_mark(4)
# # print(st1)
# #
# # st1.del_mark(2)
# # print(st1)
# #
# # st1.edit_mark(1, 5)
# # print(st1)
# #
# # print(st1.average_mark())
# sts = [st1, st2]
# my_group = Group(sts, "ГК Python")
# # # print(my_group)
# #
# my_group.add_student(st3)
# # # print()
# # # print(my_group)
# #
# my_group.remove_student(1)
# # print(my_group)
# # print()
# #
# group22 = [st2]
# my_group2 = Group(group22, 'ГК Web')
# # print(my_group2)
# # print('*' * 30)
# #
# Group.change_group(my_group, my_group2, 0)
# # print(my_group)
# # print()
# # print(my_group2)
#
# file2 = 'group_list.json'
# my_group2.dump_group(file2)
# Group.upload_journal(file2)


#  ..................................Установка модулей..........................
#  pip install requests

import requests
import json


response = requests.get('https://jsonplaceholder.typicode.com/todos')
# print(response.text)
todos = json.loads(response.text)
# print(todos)

todos_by_user = {}
for todo in todos:
    if todo['completed']:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1

print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1],  reverse=True)
print(top_users)

max_complete = top_users[0][1]
print(max_complete)









