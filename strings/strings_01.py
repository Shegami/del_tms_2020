"""
Создать переменные firstname, lastname, age с соответствующими значениями
Путем сложения получить строку вида
Привет, меня зовут Иван Иванович, мне 35 лет
Вывести на экран длину строки
"""

firstname = 'Kostia'
lastname = 'Toukach'
age = 25

text = f'Привет, меня зовут {firstname} {lastname}, мне {age} лет.'

print(text)
print(
    len(text)
)
