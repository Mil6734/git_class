# from git_class.car import carclass
from git_class.car.carclass import CarClass


class ElectroCar(CarClass):
    def __init__(self, brand, model, year, runs):
        super().__init__(brand, model, year, runs)
        self.battery = 100

    def description_battery(self):
        print(f"Этот автомобиль имеет {self.battery}% мощности ")