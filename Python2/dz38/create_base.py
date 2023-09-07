from faker import Faker
from git_class.models_new.database import create_db, Session
from git_class.models_new.car import Car
from git_class.models_new.info_car import InfoCar


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    car_names = ['BMW', 'Audi', 'Mercedes', 'Lada', 'Opel', 'Ford', 'Honda', 'Lexus']

    for i in car_names:
        cars_n = Car(model=i)
        session.add(cars_n)
    session.commit()
    faker = Faker('ru_RU')

    for i in range(len(car_names)):
        colors = faker.color()
        forces = faker.random.randint(110, 250)
        names = faker.name()
        info = InfoCar(colors, forces, names)
        session.add(info)
    session.commit()
    session.close()
