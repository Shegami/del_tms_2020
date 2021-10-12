"""
Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число
"""


def sum_for_n(number):
    if number.isdigit():
        number = int(number)
        summ = 1

        for i in range(2, number):
            summ += 1 / i

        return summ

    else:
        return 'Wrong input'


def main():
    number = input(
        'Enter a number: '
    )

    result = sum_for_n(number)
    print(result)


if __name__ == '__main__':
    main()
