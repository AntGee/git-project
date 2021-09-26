class Car:
    is_police = False

    def __init__(self, color, name):
        self.name = name
        self.color = color
        self.speed = 0

    def go(self, speed=50):
        self.speed = speed
        print(f'{self.name} поехал(а) со скоростью {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановился(ась)')

    def turn(self, direction):
        if direction == 'лево' or direction == 'право':
            print(f'{self.name} повернул(а) на {direction}')
        else:
            print(f'Машина поворачивает только на лево или право')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 61:
            print(f'Ваша скорость {self.speed}, превышает допустимую норму')
        else:
            print(f'Ваша скорость {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 41:
            print(f'Ваша скорость {self.speed}, превышает допустимую норму')
        else:
            print(f'Ваша скорость {self.speed} км/ч')


class PoliceCar(Car):
    is_police = True


auto1 = PoliceCar('Синий', 'Лада')
auto1.go(45)
auto1.stop()
print()
auto2 = SportCar('Чёрный', 'Dodge viper')
auto2.go(160)
auto2.show_speed()
auto2.turn('лево')
print()
auto3 = WorkCar('Белый', 'Chevrolet')
auto3.go(55)
auto3.show_speed()
print()
auto4 = TownCar('Жёлтый', 'Opel GTS')
auto4.go(70)
auto4.show_speed()
auto4.turn('право')
