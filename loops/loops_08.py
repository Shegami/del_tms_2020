"""
Ввести два целых числа a и b ( a < b ). Вывести в порядке
возрастания все целые числа, расположенные между a и
b (включая сами числа a и b ), а также количество n этих
чисел.
"""

a = int(
    input(
        'Enter first number: '
    ))

b = int(
    input(
        'Enter second number: '
    ))

n = 0

for i in range(a, b+1):
    print(i)
    n += 1
print(
    f'number = {n}'
)
