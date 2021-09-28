"""
Ввести с клавиатуры целое число n. Получить
сумму кубов всех целых чисел от 1 до
n(включая n) используя цикл while
"""

n = abs(
    int(
        input(
            'Enter a number: '
        )
    ))

summ = 0
while n != 0:
    summ += n ** 3
    n -= 1

print(
    f'Summ = {summ}'
)
