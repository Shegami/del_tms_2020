"""
Ввести строку с клавиатуры
Если длина строки больше 5 - вывести значение на экран
Если длина строки меньше 5 - вывести строку “Need more!”
Если длина строки равна 5 - вывести строку “It is five”
"""

sttr = input()

if len(sttr) > 5:
    print(
        sttr
    )
elif len(sttr) < 5:
    print(
        'Need more!'
    )
else:
    print(
        'It is five!'
    )
