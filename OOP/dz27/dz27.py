class Check:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"Значение {value} должно быть целым положительным числом")
        instance.__dict__[self.name] = value


class Triangle:
    x = Check()
    y = Check()
    z = Check()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def triangle_valid(self):
        if self.x + self.y > self.z and self.x + self.z > self.y and self.y + self.z > self.x:
            return "существует."
        else:
            return "не существует."

    def info(self):
        print(f"Треугольник со сторонами({self.x}, {self.y}, {self.z}) {self.triangle_valid()}")
        # return self.x + self.y > self.z and self.x + self.z > self.y and \
        #     self.y + self.z > self.x


triangle = [Triangle(2, 5, 6), Triangle(5, 2, 8), Triangle(7, 3, 6)]
for i in triangle:
    i.info()
