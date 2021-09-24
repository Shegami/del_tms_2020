"""
Вычислить квадратное уравнение ax2 + bx + c = 0 (*)
D = b2 – 4ac;
x1,2 = (-b +/- sqrt (D)) / 2a
Предусмотреть 3 варианта:
1) Два действительных корня
2) Один действительный корень
3) Нет действительных корней
"""

a = float(input(
        'enter a: '))
b = float(input(
        'enter b: '))
c = float(input(
        'enter c: '))

D = b ** 2 - 4 * a * c
x1 = (-b + D ** 0.5) / (2 * a)
x2 = (-b - D ** 0.5) / (2 * a)

print(
    f'D = {D}'
)

if D > 0:
    print(
        f'Первый корень = {x1}',
        f'Второй корень = {x2}',
        sep='\n'
    )
elif D == 0:
    print(
        f'Корень = {x1}'
    )
else:
    print(
        'Корней нет'
    )
