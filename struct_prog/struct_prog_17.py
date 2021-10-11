"""
Дано число. Найти сумму и произведение его цифр.
"""


def sum_mult(number):
    summ = mult = int(number[0])

    for elem in number[1::]:
        summ += int(elem)
        mult *= int(elem)

    return summ, mult


def main():
    number = input(
        'Enter a number: '
    )

    if number.isdigit():
        summ, mult = sum_mult(number)
        print(
            f'Sum is {summ}',
            f'Multiple is {mult}',
            sep='\n'
        )
    else:
        print('Wrong input')


if __name__ == '__main__':
    main()
