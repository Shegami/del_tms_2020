"""
Пользователь вводит три числа.
Увеличьте первое число в два раза, второе число уменьшите на 3,
третье число возведите в квадрат и затем найдите
сумму новых трех чисел.
"""

first_number = int(input()) * 2
second_number = int(input()) - 3
third_number = int(input()) ** 2

summ = sum(
    [
        first_number,
        second_number,
        third_number
    ]
)

print(summ)
