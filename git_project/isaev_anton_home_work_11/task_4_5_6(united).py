# 4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад.
#    А также класс «Оргтехника», который будет базовым для классов-наследников.
#    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#    В базовом классе определить параметры, общие для приведённых типов.
#    В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над предыдущим заданием.
#    Разработать методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
#    Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
#    можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых пользователем данных.
#    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#    Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class StoreMachines:
    def __init__(self, name, price, quantity, number_of_list, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_list
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за единицу': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена: {self.price} количество: {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование: ')
            unit_p = input(f'Введите цену за единицу: ')
            unit_q = input(f'Введите количество: ')
            unique = {'Модель устройства': unit, 'Цена за единицу': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список: {self.my_store}')
        except:
            return f'Ошибка ввода данных'
        print(f'Для выхода: Q\nПродолжение: Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад: {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMachines.reception(self)


class Printer(StoreMachines):
    def to_print(self):
        return f'Печатает {self.numb} раз/а'


class Scanner(StoreMachines):
    def to_scan(self):
        return f'Сканирует {self.numb} раз/а'


class Copier(StoreMachines):
    def to_copier(self):
        return f'Ксерокопирует {self.numb} раз/а'


p = Printer('HP', 4500, 5, 7)
s = Scanner('Canon', 3300, 5, 10)
c = Copier('Xerox', 2400, 3, 5)
p.reception()
s.reception()
c.reception()
print(p.to_print())
print(s.to_scan())
print(c.to_copier())
