from math import pi

figures = {
    'Окружность': lambda x: pi * x ** 2,
    'Прямоугольник': lambda a, b: a * b,
    'Трапеция': lambda a: lambda b: lambda h: ((a + b) * h) / 2
}

print("Площадь окружности радиуса 2:", figures['Окружность'](2))
print("Площадь прямоугольника размером 10*13:", figures['Прямоугольник'](10, 13))
print("Площадь трапеции для a=7, b=5, h=3:", figures['Трапеция'](7)(5)(3))