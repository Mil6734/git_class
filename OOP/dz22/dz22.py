import re


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, surname, num, percent, value=0):
        self.verify_surname(surname)
        self.verify_num(num)
        self.verify_percent(percent)
        self.verify_value(value)

        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value
        print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')

    @staticmethod
    def verify_surname(surname):
        if not isinstance(surname, str):
            raise TypeError("Фамилия должна быть строкой")
        a = surname.split()
        if len(a) != 1:
            raise TypeError("Введите только фамилию")
        letters = "".join(re.findall(r'[a-zа-яё-]', surname, re.IGNORECASE))
        for i in a:
            if len(i.strip(letters)) != 0:
                raise TypeError("Можно использовать только буквы")
        if len(surname) <= 2:
            raise TypeError("Проверьте введенные данные")

    @staticmethod
    def verify_num(num):
        if not isinstance(num, str):
            raise TypeError("Номер счета должен быть строкой")
        s = num.split()
        if len(s) != 1 or len(s[0]) != 5:
            raise TypeError("Номер счета введен не правильно")
        for p in s:
            if not p.isdigit():
                raise TypeError("Номер счета должны быть числовым")

    @staticmethod
    def verify_percent(percent):
        if not isinstance(percent, float):
            raise TypeError("Проценты должны быть вещественным числом")

    @staticmethod
    def verify_value(value):
        if not isinstance(value, int) or value <= 99:
            raise TypeError(f"Счет можно открыть минимум на 100{Account.suffix}")

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}.")

    def edit_owner(self, surname):
        self.surname = surname

    def add_percents(self):
        self.value += self.value * self.percent
        print('Проценты были начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято!")
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def print_balance(self):
        print(f"Текущий баланс: {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)


acc = Account("Долгих", "12345", 0.03, 1000)
acc.print_info()

acc.convert_to_usd()
acc.convert_to_eur()
print()

acc.set_usd_rate(2)
acc.convert_to_usd()

acc.set_eur_rate(3)
acc.convert_to_eur()
print()

acc.edit_owner("Дюма")
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(800)
print()

acc.add_money(5000)
print()
