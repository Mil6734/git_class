from sqlalchemy import Column, Integer, String
from git_class.models_new.database import Base


class InfoCar(Base):
    __tablename__ = 'info'

    id = Column(Integer, primary_key=True)
    color = Column(String(100), nullable=False)
    force = Column(Integer, nullable=False)
    name_owner = Column(String(100), nullable=False)

    def __repr__(self):
        return f"Информация (Цвет: {self.color}, Лошадиные силы: {self.force}, Имя владельца: {self.naem}"
