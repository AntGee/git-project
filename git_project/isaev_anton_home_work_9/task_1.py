import time


class TrafficLight:
    def start(self):
        while True:
            self.__color = 'Красный'
            print(f'\r\033[31m{self.__color}', end='')
            time.sleep(7)
            self.__color = 'Жёлтый'
            print(f'\r\033[33m{self.__color}', end='')
            time.sleep(2)
            self.__color = 'Зелёный'
            print(f'\r\033[32m{self.__color}', end='')
            time.sleep(7)


tr_light = TrafficLight()
tr_light.start()
