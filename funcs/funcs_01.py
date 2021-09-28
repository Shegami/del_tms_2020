"""
Написать функцию, которая получает на вход
имя и выводит строку вида: “Hello, {name}”.
Создать список из 5 имен. Вызвать функцию
для каждого элемента списка в цикле.
"""


def hello_name(names):
    for name in names:
        print(
            f'Hello, {name}'
        )


def main():
    names = ['Alex', 'Petya', 'Henry', 'Dick', 'Andry']
    hello_name(names)


if __name__ == '__main__':
    main()
