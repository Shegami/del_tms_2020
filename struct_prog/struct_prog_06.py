"""
Ввести строку. Если длина строки больше 10 символов, то создать новую
строку с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
Если меньше 10, то вывести на экран второй символ строки
"""


def len_of_string(string):
    if len(string) > 10:
        new_string = string + '!!!'
        return new_string

    elif len(string) < 10:
        return string[1]

    else:
        return 'Wrong input'


def main():
    string = input(
        'Enter a string: '
    )
    result = len_of_string(string)

    print()
    print(
        f'{result}'
    )


if __name__ == '__main__':
    main()
