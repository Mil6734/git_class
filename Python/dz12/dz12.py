# .....................Вариант 1........................
# def cuboid_ribs(a, b, c):
#     def cuboid_s(x, y):
#         return x * y
#
#     s = 2 * (cuboid_s(a, b) + cuboid_s(a, c) + cuboid_s(b, c))
#     return s
#
#
# print("Тестовые значения:\n2,4,6\n5,8,2\n1,6,8")
# print()
# print(cuboid_ribs(2, 4, 6))
# print(cuboid_ribs(5, 8, 2))
# print(cuboid_ribs(1, 6, 8))

# .....................Вариант 2........................
#
# s = 0
#
#
# def cuboid_ribs(a, b, c):
#
#     def cuboid_s(x, y):
#         return x * y
#
#     global s
#     s = 2 * (cuboid_s(a, b) + cuboid_s(a, c) + cuboid_s(b, c))
#
#
#
# print("Тестовые значения:\n2,4,6\n5,8,2\n1,6,8")
# print()
# cuboid_ribs(2, 4, 6)
# print(s)
# cuboid_ribs(5, 8, 2)
# print(s)
# cuboid_ribs(1, 6, 8)
# print(s)


# .....................Вариант 3........................

# def cuboid_ribs(a, b, c):
#     s = 0
#
#     def cuboid_s(x, y):
#         nonlocal s
#         s += x * y
#
#     cuboid_s(a, b)
#     cuboid_s(a, c)
#     cuboid_s(b, c)
#     return s * 2
#
#
# print("Тестовые значения:\n2,4,6\n5,8,2\n1,6,8")
# print()
# print(cuboid_ribs(2, 4, 6))
# print(cuboid_ribs(5, 8, 2))
# print(cuboid_ribs(1, 6, 8))
