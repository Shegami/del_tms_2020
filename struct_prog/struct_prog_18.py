"""
Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300.
"""


def friendly_numbers(start, stop):
    friendly_numbers_list = []

    for number in range(start, stop):
        if number not in friendly_numbers_list:

            summ = 0
            for i in range(1, number):
                if number % i == 0:
                    summ += i
            friendly_number = summ

            summ = 0
            for q in range(1, friendly_number):
                if friendly_number % q == 0:
                    summ += q

            if summ == number:
                friendly_numbers_list.append(number)
                friendly_numbers_list.append(friendly_number)

    return friendly_numbers_list


def main():
    start = 200
    stop = 300

    result = friendly_numbers(start, stop)
    print(result)


if __name__ == '__main__':
    main()
