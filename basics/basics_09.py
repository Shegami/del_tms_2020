"""
Даны два числа.
Найти среднее арифметическое и среднее геометрическое этих чисел.
"""

first_number = 4
second_number = 7

avg_arith = sum(
    [
        first_number,
        second_number
    ]
) / 2

avg_geom = (first_number * second_number) ** 0.5

print(
    avg_arith,
    avg_geom,
    sep='\n'
)
