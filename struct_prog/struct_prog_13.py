"""
Дан словарь: {'test': 'test_value', 'europe': 'eur',
'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа
(пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
Чтобы получить список ключей - использовать метод .keys()
предоставить 2 решения. Одно с использованием цикла while,
другое с использованием цикла for с параметром.
Оба решения предоставить в одном файле.
"""


def keys_editor_for(dictionary):
    for key in list(dictionary.keys()):
        dictionary[key + str(len(key))] = dictionary.pop(key)

    return dictionary


def keys_editor_while(dictionary):
    i = 0
    listt = list(dictionary.keys())

    while i < len(listt):
        dictionary[listt[i] + str(len(listt[i]))] = dictionary.pop(
            listt[i]
        )
        i += 1

    return dictionary


def main():
    dictionary = {
        'test': 'test_value',
        'europe': 'eur',
        'dollar': 'usd',
        'ruble': 'rub'
    }

    #  print(
    #     keys_editor_for(dictionary)
    # )

    print(
        keys_editor_while(dictionary)
    )


if __name__ == '__main__':
    main()
