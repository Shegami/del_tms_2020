"""
Написать игру. Пользователь должен угадать число.
Сперва вводиться диапазон угадывания. После
колличество попыток. В случае правильного ответа -
выводить You are the winner. В случае неправильного
давать игроку подсказку(больше или меньше искомое
число). Если за указанное количество попыток число не
угадано - выводить: You are the loser и правильное число.
"""

import random


def random_number(start, stop):
    return random.randrange(start, stop)


def main():
    start = int(input(
        'Enter a start point: '))
    stop = int(input(
        'Enter a stop point: '))
    tries = int(input(
        'Enter a number of tries: '))

    the_number = random_number(
        start,
        stop
    )

    for i in range(tries+1):
        player_number = int(input('Enter a number: '))
        if player_number == the_number:
            print('You are the winner')
            break
        else:
            if i < tries:
                if player_number < the_number:
                    print('More')
                else:
                    print('Less')
                print()
    else:
        print(
            'You are the loser'
        )
        print(
            f'The number was {the_number}'
        )


if __name__ == '__main__':
    main()
