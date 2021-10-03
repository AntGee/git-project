# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число».
# Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта.
# Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров.
# Проверить корректность полученного результата.


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма равна: {(self.a + other.a) + (self.b + other.b)} * i'

    def __mul__(self, other):
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'{self.a} + {self.b} * i'


c_1 = ComplexNumber(1, -2)
c_2 = ComplexNumber(3, 7)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)
