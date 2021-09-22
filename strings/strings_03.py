"""
Создать произвольную строку.
Получить подстроку с третьего элемента и до конца.
Написать два решения с использованием полной и сокращенной записи.
"""

my_string = 'This is my string. No one cannot take it'

print(
    my_string[2:],
    my_string[2:len(my_string)],
    sep='\n'
)
