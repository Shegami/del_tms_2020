"""
Дан список целых чисел.
Создать новый список, каждый элемент которого равен исходному элементу
умноженному на -2
"""


def multiple_numbers(listt):
    new_list = list()

    for elem in listt:
        new_list.append(elem * -2)

    return new_list


def main():
    listt = [1, 12, 23, 81, 34, 64]

    print(
        multiple_numbers(listt)
    )


if __name__ == '__main__':
    main()
