"""
В семье N свадьба. Они решили выбрать заведение, где будут праздновать в
зависимости от количества людей, которое прибудет к утру.
Если их будет больше 50 - закажут ресторан, если от 20 до 50 -то кафе, а
если меньше 20 то отпраздную дома.
Вывести "ресторан", "кафе", "дом" в зависимости от количества гостей
(прочитать переменную с консоли)
"""


def place_for_wedding(number_of_guests):
    if number_of_guests.isdigit():
        number_of_guests = int(number_of_guests)

        if number_of_guests > 50:
            return 'restaurant'
        elif 20 < number_of_guests < 50:
            return 'cafe'
        else:
            return 'house'
    else:
        return 'Wrong input'


def main():
    number_of_guests = input(
        'Enter an amount of guests: '
    )
    place = place_for_wedding(number_of_guests)

    print()
    print(
        f'The wedding will be at {place}'
    )


if __name__ == '__main__':
    main()
