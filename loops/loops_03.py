"""
Просуммировать неопределенное количество чисел,
вводимых пользователем, суммировать до тех пор, пока
пользователь не введёт слово «stop»
"""

summ = 0

while True:
    number = input(
        'Enter a number: '
    )
    if number == 'stop':
        break
    elif number.isdigit():
        summ += float(number)
        continue
    else:
        print(
            'Wrong input!'
        )
        continue

print(
    f'Sum = {summ}'
)
