class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}')


stationery1 = Stationery('')
stationery1.draw()
pen1 = Pen('землю')
pen1.draw()
pencil1 = Pencil('землю')
pencil1.draw()
handle1 = Handle('землю')
handle1.draw()
