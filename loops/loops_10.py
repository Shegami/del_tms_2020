"""
Создать квадратную матрицу размерностью n
и заполнить ее случайными значениями.
Найти сумму всех элементов матрицы,
которые кратны 3
"""

from random import randint

n = int(
    input(
        'Enter a number: '
    )
)
matrix = []
summ = 0

for i in range(n):
    row = []
    for column in range(n):
        row.append(
            randint(1, 9)
        )
    matrix.append(row)
    print(row)

for row in matrix:
    for element in row:
        if element % 3 == 0:
            summ += element

print(summ)
