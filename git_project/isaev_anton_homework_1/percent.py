percent = int(input('Введите процент от 1 до 100: '))

percent_list = ['процент', 'процента', 'процентов']

if percent == 1:
    print(f'{percent} {percent_list[0]}')
elif 1 < percent < 5:
    print(f'{percent} {percent_list[1]}')
elif 5 <= percent <= 100:
    print(f'{percent} {percent_list[2]}')
