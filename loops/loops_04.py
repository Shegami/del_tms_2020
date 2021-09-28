"""
Просуммировать неопределенное количество чисел,
вводимых пользователем, суммировать до тех пор, пока
пользователь не введёт слово «стоп». Не учитывать
числа кратные 5
"""

summ = 0

while True:
    number = input(
        'Enter a number: '
    )
    if number == 'stop':
        break
    elif number.isdigit():
        if float(number) % 5 != 0:
            summ += float(number)
        continue
    else:
        print(
            'Wrong input!'
        )

print(
    f'Sum = {summ}'
)
