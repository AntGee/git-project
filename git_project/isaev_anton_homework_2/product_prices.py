price_list = [12, 55.80, 23.50, 5, 92.30, 34.20, 50, 73.13, 34.12, 93.72, 5.94, 9.25, 68, 19.99, 99.99, 75.35]
new_price_list = []

for i in price_list:
    rubles = int(i)
    kop = round((i - rubles) * 100)
    new_price_list.append(f'{rubles} руб {kop:02d} коп')

print(', '.join(new_price_list))

id1 = id(price_list)
price_list.sort()
print(price_list)

print(id(price_list) == id1)

price = sorted(price_list, reverse=True)
print(sorted(price[:5]))
