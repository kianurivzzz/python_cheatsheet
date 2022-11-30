'''
-----------------------------------------------RU----------------------------------------------------------------
Цикл for..in осуществляет итерацию по последовательности объектов,
т.е. проходит через каждый элемент в последовательности.
Последовательность – это упорядоченный набор элементов.

Сначала записывается ключевое слово for, потом переменная счётчик,
после переменной пишется ключевое слово in, а в конце последовательность (например, 1, 2, 3)
и строками ниже записывается тело цикла с *отступом.

*4 пробела или 1 табуляция

------------------------------------------------EN---------------------------------------------------------------
The for...in loop iterates through a sequence of objects,
i.e. it goes through each element in the sequence.
A sequence is an ordered set of elements.

First the keyword for is written, then the variable counter,
after the variable we write the keyword in and at the end of it the sequence (for example, 1, 2, 3)
and lines below it, the body of the loop is indented.

*4 spaces or 1 tab

'''

for i in 1, 2, 3:
    print(i)
#Вывод:
#1
#2
#3


# или

for i in 'строка', 'и я строка', 'мы строки':
    print(i)
#Вывод:
#строка
#и я строка
#мы строки


# или

for i in range(1, 3):
    print(i)
# Вывод:
#1
#2
#в функции range последнее число не включается в последовательность!!!


# py for.py - запуск файла/file run
