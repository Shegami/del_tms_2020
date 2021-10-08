"""
Дан список целых чисел. Подсчитать сколько четных чисел в списке
"""


def counter_of_even(listt):
    counter = 0

    for elem in listt:
        if elem % 2 == 0:
            counter += 1

    return counter


def main():
    listt = [1, 21, 72, 45, 14]

    print(
        counter_of_even(listt)
    )


if __name__ == '__main__':
    main()
