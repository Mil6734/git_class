import math


class Arg:

    @staticmethod
    def min_arg(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def max_arg(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def arif_arg(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial_arg(n):
        return math.factorial(n)


print(f"Минимальное число: {Arg.min_arg(3, 5, 7, 9)}")
print(f"Максимальное число: {Arg.max_arg(3, 5, 7, 9)}")
print(f"Среднее арифметическое: {Arg.arif_arg(3, 5, 7, 9)}")
print(f"Факториал числа: {Arg.factorial_arg(5)}")
