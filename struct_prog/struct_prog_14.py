"""
Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 -> 2 3 4 5 1

Предоставить 2 решения. Одно с использованием цикла while,
другое с использованием цикла for с параметром.
Оба решения предоставить в одном файле
"""


def list_moved_for(some_list):
    index = 0
    for elem in list(some_list):
        some_list[index - 1] = elem
        index += 1

    return some_list


def list_moved_while(some_list):
    index = 0
    listt = some_list[:]

    while index < len(listt):
        some_list[index - 1] = listt[index]
        index += 1

    return some_list


def main():
    listt = [1, 2, 3, 4, 5]

    print(
        list_moved_while(listt)
    )


if __name__ == '__main__':
    main()
