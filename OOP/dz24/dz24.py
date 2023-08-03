class Student:
    def __init__(self, name):
        self.name = name
        self.model = self.Laptop()

    def show(self):
        print(f'{self.name} => {self.model.show()}')

    class Laptop:
        def __init__(self):
            self.model = "HP"
            self.processor = "I7"
            self.memory = 16

        def show(self):
            return f"{self.model}, {self.processor}, {self.memory}"


student1 = Student("Roman")
student1.show()

student2 = Student("Vladimir")
student2.show()