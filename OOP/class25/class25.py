# перегрузка операторов
# 24 * 60 * 60 = 86400(СЕКУНД В ОДНОМ ДНЕ)

class Clock:
    __DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{self.get_form(h)}:{self.get_form(m)}:{self.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __eq__(self, other):
        # if self.sec == other.sec:
        #     return True
        # return False
        return self.sec == other.sec


c1 = Clock(100)
c2 = Clock(100)
if c1 == c2:
    print("время равно")
else:
    print("время разное")

# print(c1.get_format_time())
# print(c2.get_format_time())
#
# c3 = c1 + c2
# print(c3.get_format_time())
