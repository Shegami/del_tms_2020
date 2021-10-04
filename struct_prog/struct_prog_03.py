"""
Получить на ввод количество рублей и копеек и вывести в правильной
форме, например, 3 рубля, 1 рубль 25 копеек, 3 копейки
"""


def amount_to_dct(amount):
    dct_int_flt = {
        'integer': None,
        'float': None
    }

    if '.' in amount:
        amount = amount.split('.')
        dct_int_flt['integer'] = int(amount[0])
        dct_int_flt['float'] = int(amount[1])
    else:
        dct_int_flt['integer'] = int(amount)

    return dct_int_flt


def rubles(dct_amount):
    number = dct_amount['integer']

    if 10 < number % 100 < 15:
        return 'рублей'
    elif 1 < number % 10 < 5:
        return 'рубля'
    elif number % 10 == 1:
        return 'рубль'
    else:
        return 'рублей'


def cents(dct_amount):
    if dct_amount['float']:
        number = dct_amount['float']

        if 10 < number % 100 < 15:
            return 'копеек'
        elif 1 < number % 10 < 5:
            return 'копейки'
        elif number % 10 == 1:
            return 'копейка'
        else:
            return 'копеек'
    else:
        return False


def main():
    amount = input(
        'Enter an amount: '
    )
    dct_amount = amount_to_dct(amount)
    amount_rubles = rubles(dct_amount)
    amount_cents = cents(dct_amount)

    if amount_cents:
        print(
            f"{dct_amount['integer']} {amount_rubles} "
            f"{dct_amount['float']} {amount_cents}"
        )
    else:
        print(
            f"{dct_amount['integer']} {amount_rubles}"
        )


if __name__ == '__main__':
    main()
