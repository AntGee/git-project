time = int(input('Введите число, где 1 = 1 секунде: '))

if time < 60:
    second = time % 60
    print(f'{second} секунд')
elif 60 <= time < 3600:
    second = time % 3600
    minute = time // 60
    second %= 60
    print(f'{minute}:{second}, mm:ss формат')
elif 86400 > time >= 3600:
    second = time % (24 * 3600)
    hour = second // 3600
    second %= 3600
    minute = second // 60
    second %= 60
    print(f'{hour}:{minute}:{second}, hh:mm:ss формат')
else:
    day = time // 86400
    second = time % (24 * 3600)
    hour = second // 3600
    second %= 3600
    minute = second // 60
    second %= 60
    print(f'{day}:{hour}:{minute}:{second}, dd:hh:mm:ss формат')

# Сделал 2-ой вариант этого задания, через создания собственной функции:

time = int(input('Введите число, где 1 = 1 секунде: '))


def time_conversion():
    day = time // 86400
    sec = time % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    print(f'{day}:{hour}:{minute}:{second}, dd:hh:mm:ss формат')
    return '%02d:%02d:%02d:%02d' % (day, hour, min, sec)


print(time_conversion())
