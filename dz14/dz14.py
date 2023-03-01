#   ...................Задача 1....................

# def dec_main(args1):
#     def dec(fn):
#         def args_dec(*args):
#             print(args1, args, "=", end=" ")
#             fn(*args)
#
#         return args_dec
#     return dec
#
#
# @dec_main("Сумма чисел")
# def summ(*num):
#     print(sum(num))
#
#
# @dec_main("Среднее арифметическое чисел")
# def ave(*num):
#     print(sum(num) / len(num))
#
#
# summ(2, 3, 3, 4)
# ave(2, 3, 3, 4)


#   ...................Задача 2....................


# def change_to_str(s, c_old, c_now):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old and i % 2 == 0:
#             s2 = s2 + c_now
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = change_to_str(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)


#   ...................Задача 3....................

# def fn(n, pos):
#     if pos < 0 or pos >= len(n):
#         return n
#
#     return n[:pos] + n[pos + 1:]
#
#
# s = '0123456789'
# s2 = fn(s, 5)
# print("s =", s)
# print("s2 =", s2)


#   ...................Задача 4....................

# def fn(n, c):
#     x = ""
#
#     for i in n:
#         if i != c:
#             x += i
#     return x
#
#
# s = '012345363738494'
# s2 = fn(s, '3')
#
# print("s =", s)
# print("s2 =", s2)
