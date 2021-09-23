"""
Ввести число с клавиатуры. Вернуть результат логического выражения: число
больше 15 и число кратно 5.
"""

numb = float(input('input a number: '))

print(f'the number is bigger than 15? {numb > 15}')
print(f'the number is multiple to 5? {numb % 5 == 0}')
