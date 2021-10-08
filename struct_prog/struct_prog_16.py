"""
Написать программу, в которой вводятся два операнда Х и Y и знак операции
sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
реакции на возможный неверный знак операции, а также на ввод Y=0 при
делении. Организовать возможность многократных вычислений без
перезагрузки программа (т.е. построить бесконечный цикл). В качестве
символа прекращения вычислений принять ‘0’ (т.е. sign='0')
"""


def calculator():
    while True:
        sign = input(
            'Enter a sign: '
        )

        if sign == '0':
            print('The end.')
            break

        else:
            if sign != '/' and '+' and '*' and '-':
                print('Wrong sign')

            else:
                x = float(input(
                    'Enter the first number: '
                ))

                y = float(input(
                    'Enter the second number: '
                ))

                if sign == '+':
                    print(x + y)

                elif sign == '-':
                    print(x - y)

                elif sign == '/':
                    if y != 0:
                        print(x / y)
                    else:
                        print('Wrong input')

                elif sign == '*':
                    print(x * y)

                elif sign == '0':
                    print('The end')


def main():
    calculator()


if __name__ == '__main__':
    main()
