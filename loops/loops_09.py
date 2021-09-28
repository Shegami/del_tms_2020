"""
Создать квадратную матрицу размерностью n
и заполнить ее случайными значениями от 1
до 9
"""

from random import randint

n = int(
    input(
        'Enter a number: '
    )
)
matrix = []

for raw in range(n):
    matrix.append(
        list()
    )
    for column in range(n):
        matrix[raw].append(
            randint(1, 9)
        )
    print(matrix[raw])
