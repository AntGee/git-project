# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return divider / denominator
        except ZeroDivisionError:
            return f'Деление на ноль недопустимо'


div = DivisionByZero(10, 100)
print(DivisionByZero.divide_by_zero(10, 0))
print(div.divide_by_zero(100, 0))
print(DivisionByZero.divide_by_zero(100, 10))
print(div.divide_by_zero(462, 7))
