#   ..............Задача 1.......................

# tpl = ('ab', 'abcd', 'cde', 'abc', 'def')
# print("Исходный корте: ", tpl)
# s = input("s = ")
# if s in tpl:
#     print("yes")
# else:
#     print("no")

#   ................Задача 2.....................

tpl = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
print(tpl)
tpl_el = set(tpl)
for i in tpl_el:
    print('Количество', i, '=', tpl.count(i))


