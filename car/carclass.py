class CarClass:
    def __init__(self, brand, model, year, runs):
        self.brand = brand
        self.model = model
        self.year = year
        self.runs = runs

    def show_car(self):
        print(f"{self.brand}, {self.model}, {self.year} год, {self.runs} km")


if __name__ == '__main__':
    car1 = CarClass('Tesla', 'T', 2020, 34000)
    car1.show_car()