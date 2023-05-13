# print(ord('a'))   # из символа преобразует в код

# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# my_str = "Test string for me"
# arr = [ord(i) for i in my_str]
# print("ASCII коды: ", arr)
#
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
#
# arr += [ord(x) for x in input('->')[:3] if ord(x) not in arr]
# print(arr)
#
# print("Количество последних элементов", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(7))  # из кода преобразует в символ


# a = 122
# b = 97
# code = [chr(i) for i in range(b, a + 1)]
# print(code)


# print('apple' == 'Apple')  # 97 == 65
# print('apple' > 'Apple')  # 97 > 65


# from random import randint
#
# short = 7
# long = 10
# min_ASCII = 33
# max_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(short, long)
#     res = ""
#     for i in range(rand_len):
#         rand_char = chr(randint(min_ASCII, max_ASCII))
#         res += rand_char
#
#     return res
#
#
# print("Случайный пароль: ", random_password())


# ..............Методы строк.................

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.

# print(s.count('h'))  # подсчет количества вхождений подстроки в строку(2)
# print(s.find("Python"))  # Возвращает первый индекс, который соответствует началу подстроки или -1 элемента нет
# print(s.index('Python'))  # Возвращает первый индекс, который соответствует началу подстроки
# или ValueError если элемента нет
# print(s.rindex('h'))  # Возвращает последний индекс


# s1 = 'ab12c59p7dq'
# digits = []
# for symbol in s1:
#     if '123456789'.find(symbol) != -1:
#         digits.append(int(symbol))
#
# print(digits)


# s = "hello, WORLD! I am learning Python."
# print(s.endswith('on.'))  # На что заканчивается строка, возвращает True and False
# print(s.startswith('h'))  # На что начинается строка, возвращает True and False

# print('abc123'.isalnum())  # Состоит ли строка из букв и цифр возвращает True and False
# print('abcABC'.isalpha())  # Состоит ли строка из букв возвращает True and False
# print('1234'.isdigit())  # Состоит ли строка из цифр возвращает True and False

# print('abc12'.islower())  # определяет состоит ли строка из символов букв в нижмем регистре
# # (могут присутствовать любые символы
# print('abc12'.isupper())  # определяет состоит ли строка из символов букв в верхнем регистре
# # (могут присутствовать любые символы


