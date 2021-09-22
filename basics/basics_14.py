"""
Пользователь вводит цены 1 кг конфет и 1 кг печенья. Найдите стоимость:
а) одной покупки из 300 г конфет и 400 г печенья;
б) трех покупок, каждая из 2 кг печенья и 1 кг 800 г конфет.
"""

sweets = float(input('price sweets: '))
cookies = float(input('price cookies: '))

a = sweets * 0.3 + cookies * 0.4
b = 3 * (sweets * 2 + cookies * 1.8)

print(
    f'first buy price: {a}',
    f'second buy price: {b}',
    sep='\n'
)
