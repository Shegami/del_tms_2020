"""
Создать список с фамилиями. Вывести все фамилии,
которые начинаются на П и заканчиваются на а
"""


def last_names(lastnames):
    listt = []
    for lastname in lastnames:
        if lastname[0] == 'П' and lastname[-1] == 'а':
            listt.append(lastname)
    return listt


def main():
    lastnames = [
        'Петрович',
        'Алексеевич',
        'Пашаняна',
        'Павлова'
    ]

    listt = last_names(lastnames)
    for lastname in listt:
        print(lastname)


if __name__ == '__main__':
    main()
