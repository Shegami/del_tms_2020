"""
Пользователь вводит значение температуры в градусах Цельсия. Вывести
температуру в градусах Фаренгейта.
"""

temp_celsius = float(input('temp (celsius): '))

temp_fahrenheit = temp_celsius * 1.8 + 32

print(f'temperature Fahrenheit: {temp_fahrenheit}')
