"""
Ввести строку. Вывести на экран букву, которая находится в середине этой
строки.
Также, если эта центральная буква равна первой букве в строке, то создать и
вывести часть строки между первым и последним символами исходной
строки.
(подсказка: для получения центральной буквы, найдите длину строки и
разделите ее пополам. Для создания результирующий строки используйте
срез)
"""


def middle_index(string):
    index = int(
        len(string) / 2
    )

    return index


def first_mid_same(string, index):
    if string[0] == string[index]:

        return string[1:index]


def main():
    string = input(
        'Enter a string: '
    )

    index = middle_index(string)
    print(string[index])

    if first_mid_same(string, index):
        print(
            f'{string[1:index]}'
        )


if __name__ == '__main__':
    main()
