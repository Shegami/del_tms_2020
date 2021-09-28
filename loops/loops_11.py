"""
Дан двумерный массив n × m элементов. Определить,
сколько раз встречается число 7 среди элементов
массива
"""

from random import randint

n = int(input(
    'Enter a number of rows: '))
m = int(input(
    'Enter a number of columns: '))
matrix = []
counter = 0

for i in range(n):
    row = []
    for column in range(m):
        row.append(
            randint(1, 9)
        )
    matrix.append(row)

for row in matrix:
    for element in row:
        if element == 7:
            counter += 1

for row in matrix:
    print(row)
print(counter)
