"""
Введите число. Если это число делиться на 1000 без остатка, то выведите на
экран "millennium"
"""


def millennium(number):
    if number.isdigit():
        if float(number) % 1000 == 0:
            return 'Millennium'
        else:
            return 'Not millennium'
    else:
        return 'Wong input'


def main():
    number = input(
        'Enter an amount: '
    )

    print(
        millennium(number))


if __name__ == '__main__':
    main()
