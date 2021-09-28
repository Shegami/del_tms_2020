"""
Получить сумму кубов натуральных чисел от n
до m используя цикл for
"""

from random import randint

n = randint(1, 5)
m = randint(6, 9)
summ = 0

for i in range(n, m):
    summ += i ** 3

print(
    f'summa = {summ}'
)
