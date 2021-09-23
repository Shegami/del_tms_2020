"""
Ввести число, проверить на то, что было введено именно
число. Возвести его в куб и вывести результат на экран.
"""

number = input(
    'enter a number: '
)

if number.isdigit():
    print(
        float(number) ** 3
    )
else:
    print(
        'Not digit'
    )
