"""
Ввести почтовый адрес. Проверить доменное имя. В случае если оно
gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
“DOMAIN NAME is not supported’
"""

email = input()

if '@' in email:
    if email.split('@')[1] == 'gmail.com':
        print(
            email)
else:
    print(
        'DOMAIN NAME is not supported')
