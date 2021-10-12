"""
Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число
больше предыдущего).
"""

from random import randrange


def growth_counter(some_list):
    counter = 0

    for index, value in enumerate(some_list[1::], start=1):
        if index < len(some_list) - 1:
            if some_list[index - 1] < value >= some_list[index + 1]:
                counter += 1

        else:
            if value > some_list[index - 1]:
                counter += 1

    return counter


def main():
    some_list = []

    for i in range(10):
        some_number = randrange(1, 10)
        some_list.append(some_number)

    print(some_list)
    print(
        growth_counter(some_list)
    )


if __name__ == '__main__':
    main()
