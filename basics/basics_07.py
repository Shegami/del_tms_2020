"""
Даны действительные числа x и y. Получить (|x| - |y|) / (1 + |x * y|)
Для нахождения модуля использовать функцию abs(..)
"""

x = int(input('input first number: '))
y = int(input('input first number: '))

print(
    (abs(x) - abs(y)) / (1 + abs(x * y))
)
