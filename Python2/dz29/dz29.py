import csv
import re


data = {
    "Россия": "Москва",
    "Беларусь": "Минск",
    "Франция": "Париж"
}


def add_data(count, cap):
    data[count] = cap
    print("Файл сохранен")


def del_data(count):
    if count in data:
        del data[count]
        print("Данные удалены")
    else:
        print("Такой страны нет")


def search_data(count):
    if count in data:
        print(f"Страна {count}, столица {data[count]}")
    else:
        print("Такой страны нет в словаре")


def edit_data(count, new_cap):
    if count in data:
        data[count] = new_cap
        print("Данные исправлены")
    else:
        print("Такой страны нет в словаре")


def view_data():
    for count, cap in data.items():
        print("Страна: ", count)
        print("Столица: ", cap)
        print("-" * 30)


def check_country(count):
    reg = "[А-ЯЁ][а-яё]+$"
    return re.match(reg, count)


def check_capital(cap):
    reg = "[А-ЯЁ][а-яё]+$"
    return re.match(reg, cap)


while True:
    print("*" * 30, "\nВыбор действия:")
    print("1 - добавление данных\n2 - удаление данных\n3 - поиск данных"
          "\n4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы")

    choice = int(input("Ввод: "))

    if choice == 1:
        country = input("Введите название страны: ")
        capital = input("Введите название столицы страны: ")
        if check_country(country) and check_capital(capital):
            add_data(country, capital)
        else:
            print('Не корректный ввод данных, повторите попытку')

    elif choice == 2:
        country = input("Введите название страны: ")
        if check_country(country):
            del_data(country)
        else:
            print('Не корректный ввод данных, повторите попытку')

    elif choice == 3:
        country = input("Введите название страны: ")
        if check_country(country):
            search_data(country)
        else:
            print('Не корректный ввод данных, повторите попытку')

    elif choice == 4:
        country = input("Введите название страны: ")
        capital = input("Введите название столицы страны: ")
        if check_country(country) and check_capital(capital):
            edit_data(country, capital)
        else:
            print('Не корректный ввод данных, повторите попытку')

    elif choice == 5:
        view_data()

    elif choice == 6:
        print("Работа завершена")
        break
    else:
        print("Некорректные данные, повторите попытку")


with open("countries.csv", "w") as f:
    writer = csv.writer(f, delimiter=';', lineterminator='\r')
    writer.writerow(["Страна", "Столица"])
    for item in data.items():
        writer.writerow(item)
