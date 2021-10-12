"""
В массиве целых чисел с количеством элементов 19 определить
максимальное число и заменить им все четные по значению элементы.
"""

from random import randrange


def max_elem(some_list):
    max_number = some_list[0]

    for elem in some_list[1:]:

        if elem > max_number:
            max_number = elem

    for index, value in enumerate(some_list):
        if value % 2 == 0:
            some_list[index] = max_number

    return some_list


def main():
    some_list = []

    for i in range(19):
        random_number = randrange(1, 1000)
        some_list.append(random_number)

    result = max_elem(some_list)
    print(result)


if __name__ == '__main__':
    main()
