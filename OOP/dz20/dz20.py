class Auto:

    def __init__(self, name, year, manufacturer, power, color, price):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price

    def __check_numbers(z):
        if isinstance(z, int):
            return True
        return False

    def __check_letters(z):
        if isinstance(z, str):
            return True
        return False

    def print_info(self):
        print(" Персональные данные ".center(40, '*'))
        print(f"Название модели: {self.name}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}\n"
              f"Мощность двигателя: {self.power} л.с.\nЦвет машины: {self.color}\nЦена : {self.price} рублей")
        print("=" * 40)

    def set_price(self, price):
        if Auto.__check_numbers(price):
            self.price = price
        else:
            print("Значение должно быть числовым")

    def get_price(self):
        return self.price

    def set_manufacturer(self, manufacturer):
        if Auto.__check_letters(manufacturer):
            self.manufacturer = manufacturer
        else:
            print("Ошибка")

    def get_manufacturer(self):
        return self.manufacturer

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


p1 = Auto("X7 M50i", 2021, "BMW", 530, "white", 10790000)
p1.print_info()

p1.name = "RS6"
p1.set_manufacturer("Audi")
p1.set_price(4000000)
p1.print_info()

