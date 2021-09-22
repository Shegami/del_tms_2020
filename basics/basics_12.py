"""
Запросить у пользователя два целых числа.
Вывести строку вида “2 плюс 3 равно 5”
Примечание: после ввода переменных преобразовать переменные к типу int
>> first_number = int(first_number)
"""

first_number = int(input('Input first number: '))
second_number = int(input('Input second number: '))

sum_numbs = sum(
    [
        first_number,
        second_number
    ]
)

print(
    f'{first_number} плюс {second_number} равно {sum_numbs}'
)
