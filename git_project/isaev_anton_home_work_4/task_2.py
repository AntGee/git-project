from requests import get


def currency_rates(name):
    site = get('http://www.cbr.ru/scripts/XML_daily.asp').text.split('</Valute>')

    for n in site:
        if n.count(name):
            nominal = int(n[n.find('<Nominal>') + len('<Nominal>'):n.find('</Nominal>')])
            value = round(float(n[n.find('<Value>') + len('<Value>'):n.find('</Value>')].replace(',', '.')), 2)
            print(f'{nominal} {name} = {value} руб')


if __name__ == '__main__':
    code_val = str(input('Введите код/название валюты: '))
    currency_rates(code_val)
