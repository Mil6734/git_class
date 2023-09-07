from sqlalchemy import Column, ForeignKey, Integer, String
from git_class.models_new.database import Base


class Car(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True)
    model = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    price = Column(Integer, ForeignKey('info.id'))

    def __repr__(self):
        return f"Модель авто: {self.model}, Возраст авто: {self.age}, Цена авто: {self.price}"
