class Shape:
    def __init__(self, color):
        self.color = color

    def info(self):
        print(f'{self.color}')

    def get_perimetr(self):
        pass

    def get_area(self):
        pass

    def draw(self):
        pass


class Square(Shape):
    def __init__(self, a, color):
        self.a = a
        super().__init__(color)

    def get_perimetr(self):
        return self.a * 4

    def get_area(self):
        return self.a * self.a

    def info(self):
        print(f"===Квадрат===\nСторона:{self.a}\nЦвет:{self.color}"
              f"\nПлощадь:{self.get_area()}\nПериметр:{self.get_perimetr()}")

    def draw(self):
        for i in range(self.a):
            for j in range(self.a):
                print("*", end="")
            print()


class Rectangle(Shape):
    def __init__(self, h, w, color):
        self.h = h
        self.w = w
        super().__init__(color)

    def get_perimetr(self):
        return 2 * (self.h + self.w)

    def get_area(self):
        return self.h * self.w

    def info(self):
        print(f"===Прямоугольник===\nДлина:{self.h}\nШирина:{self.w}\nЦвет:{self.color}"
              f"\nПлощадь:{self.get_area()}\nПериметр:{self.get_perimetr()}")

    def draw(self):
        for i in range(self.h):
            for j in range(self.w):
                print("*", end="")
            print()


class Triangle(Shape):
    def __init__(self, s1, s2, s3, color):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        super().__init__(color)

    def get_perimetr(self):
        return self.s1 + self.s2 + self.s3

    def get_area(self):
        p = (self.s1 + self.s2 + self.s3) / 2
        return round((p * (p - self.s1) * (p - self.s2) * (p - self.s3)) ** 0.5, 2)

    def info(self):
        print(f"===Треугольник===\nСторона1:{self.s1}\nСторона2:{self.s2}\nСторона3:{self.s3}"
              f"\nЦвет:{self.color}\nПлощадь:{self.get_area()}\nПериметр:{self.get_perimetr()}")

    def draw(self):
        for i in range(self.s3):
            print(" " * (self.s3 - 1 - i) + "*" * (1 + i * 2))


shape = [Square(3, 'red'), Rectangle(3, 7, "green"), Triangle(11, 6, 6, 'yellow')]
for i in shape:
    i.info()
    i.draw()
    print()

