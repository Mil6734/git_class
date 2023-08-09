# from git_class.car.electrocar import ElectroCar
#
#
# def main():
#     car = ElectroCar('Tesla', 'T', 2018, '99000')
#     car.show_car()
#     car.description_battery()
#
#
# if __name__ == '__main__':
#     main()


#  ...........................Упаковка данных(сериализация)......................
#  ........................Распаковка данных(десериализация)...................

#  marshal (*pyc)
#  pickle
#  json

# dump() - сохраняет данные в открытый файл
# load() - считывает данные из открытого файла
# dumps() - сохраняет данные в строку
# loads() - считывает данные из строки


# import pickle
#
# file_name = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['яблоко', 'манго'],
#     'овощи': ['морковь', 'огурец'],
#     'бюджет': 1000
# }
#
# with open(file_name, 'wb') as f:
#     pickle.dump(shop_list, f)
#
# with open(file_name, 'rb') as f:
#     shop_list_2 = pickle.load(f)
# print(shop_list_2)


# class Test:
#     num = 35
#     st = 'Привет'
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#     d = {'first': 'a', 'second': 2}
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nКортеж: {Test.tpl}" \
#                f"\nСловарь: {Test.d}"
#
#
# obj = Test()
# # print(obj)
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
# obj = pickle.loads(my_obj)
# print(obj)


# import pickle
#
#
# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a}, {self.b}, {self.c}'
#
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


# import json
#
# data = {
#     'name': 'Olga',
#     'age': 35,
#     20: None,
#     True: 1,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'firstname': 'Alisa',
#             'age': 6
#         }
#     ]
# }
#
# with open('data_file.json', 'w') as f:
#     json.dump(data, f, indent=4)
#
# with open('data_file.json', 'r') as f:
#     data1 = json.load(f)
# print(data1)
#
#
# json_string = json.dumps(data)
# print(json_string)
# print(json_string[2])
# print(type(json_string))
#
# data1 = json.loads(json_string)
# print(data1)
# print(type(data1))
# print(data1['name'])


# x = {
#     "name": "Виктор"
# }
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'm', 'n', 'k']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        # a = ''
        # for i in self.marks:
        #     a += str(i) + ', '
        # return f'Студент: {self.name} - {a[:-2]}'
        a = ', '.join(map(str, self.marks))
        return f'Студент: {self.name} - {a}'

    def add_mark(self, mark):
        self.marks.append(mark)

    def del_mark(self, index):
        self.marks.pop(index)


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
print(st1)
st1.add_mark(4)
print(st1)
st1.del_mark(2)
print(st1)
