# names = ["Adam", ["Bob", ["Chet", ["Cat"]], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
# n = 0
# new_names = [names]
# while new_names:
#     current = new_names.pop()
#     if isinstance(current, list):
#         for item in current:
#             new_names.append(item)
#     else:
#         n += 1
#         print(n, end=" ")

#  ............................Вариант 2...........................

names = ["Adam", ["Bob", ["Chet", ["Cat"]], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
count = 0
for i in range(len(names)):
    count += 1
    for j in range(len(names[i]) - 1):
        if isinstance(names[i], list):
            count += 1
            for k in range(len(names[i][j]) - 1):
                if isinstance(names[i][j], list):
                    count += 1
print(names)
print(count)
