"""
Ввести предложение состоящее из двух слов.
Поменять местами слова, добавить восклицательный знак в начало и конец,
вывести итоговое предложение на экран.
"""

sentence = input().split()

print(sentence)
sentence = sentence[::-1]
sentence.insert(0, '!')
sentence.insert(len(sentence) + 1, '!')

for word in sentence:
    print(word, end=' ')
