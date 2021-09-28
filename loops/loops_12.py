"""
Дана целочисленная матрица А[n,m]. Посчитать
количество элементов матрицы, превосходящих среднее
арифметическое значение элементов матрицы и сумма
индексов которых четна.
"""
from random import randrange

A = []
n = int(input(
    'Number of rows: '))
m = int(input(
    'Number of columns: '))
summ = 0
counter = 0

for i in range(n):
    row = []
    for column in range(m):
        element = randrange(9)
        row.append(element)
        summ += element
    A.append(row)
    print(row)

avg = summ / (n * m)
print(
    f'avg = {avg}'
)

for row in range(len(A)):
    for i, value in enumerate(A[row]):
        if value > avg:
            if (row + i) / 2 == 0:
                counter += 1

print(counter)
