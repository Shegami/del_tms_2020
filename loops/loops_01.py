"""
Выведите на экран n раз фразу "Silence is golden". Число
n вводит пользователь.
"""

n = int(
    input(
        'Enter a number: '
    ))

while n != 0:
    print(
        'Silence is golden'
    )
    n -= 1
