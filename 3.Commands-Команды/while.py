'''
-----------------------------------------------RU----------------------------------------------------------------
Цикл while позволяет многократно выполнять блок команд до тех пор,
пока условие записанное в нём истинно, то есть возвращает True.
Это один из 2-х циклов.
Он также может иметь необязательный пункт else.

Сначала записывается ключевое слово while, потом записывается условие (например, a < b),
после условия ставится знак двоеточия и строками ниже записывается тело цикла с *отступом.

*4 пробела или 1 табуляция

------------------------------------------------EN---------------------------------------------------------------
The while loop allows you to execute a block of commands repeatedly
as long as the condition written in it is true, i.e. it returns True,
the condition written in it is true, i.e. it returns True.
This is one of the 2 loops.
It may also have an optional else clause.

First the while keyword is written, then the condition is written (for example, a < b),
The condition is followed by a colon and the loop body is indented.

*4 spaces or 1 tab

'''

number = 23

while True: # бесконечный цикл
    guess = int(input('Введите целое число : '))

    if guess == number:
        print('Поздравляю, вы угадали.')
        break # это останавливает цикл while

    elif guess < number:
        print('Нет, загаданное число немного больше этого.')

    else:
        print('Нет, загаданное число немного меньше этого.')


# Здесь можете выполнить всё что вам ещё нужно после цикла
print('Цикл while закончен.')
print('Завершение...')

# py while.py - запуск файла/file run
