"""
Создать список произвольного содержания.
После каждой операции выводить список на экран

Добавить к нему строку “Hello”.
Удалить первый элемент.
Поменять второй элемент на строку “World”.
Удалить элемент “World”
Вывести на экран перевернутый список
"""

listt = [1, 'two', 3, 'four', 5, 'six', 'seven', 8]

listt.append('Hello')
print(listt)

listt.pop(0)
print(listt)

listt[1] = 'World'
print(listt)

listt.remove('World')
print(listt)

print(listt[::-1])
