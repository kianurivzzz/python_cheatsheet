'''
-----------------------------------------------RU----------------------------------------------------------------
Комментарии – это то, что пишется после символа #,
и нужен только для читающего программу человека. Комментарии не влияют
на работу программы. Интерпретатор их игнорирует.
Все описания в этих файлах написаны с помощью комментариев, кстати.

Старайтесь в своих программах писать как можно больше полезных комментариев, объясняющих:
- предположения;
- важные решения;
- важные детали;
- проблемы, которые вы пытаетесь решить;
- проблемы, которых вы пытаетесь избежать и т.д.

Код программы говорит о том, КАК, а комментарии должны объяснять, ПОЧЕМУ.
Это будет полезно для других разработчиков, так как им легче будет понять,
что программа делает. Помните, что таким человеком можете оказаться вы сами
через полгода!

------------------------------------------------EN---------------------------------------------------------------
Comments are what is written after the # symbol,
and is only needed for the person reading the program.
All descriptions in these files are written with comments, by the way.

Try to write as many useful comments in your programs as possible, explaining
- assumptions;
- important decisions;
- important details;
- the problems you're trying to solve;
- the problems you're trying to avoid, etc.

The program code tells you HOW, and the comments should explain WHY.
This will be useful for other developers because it will be easier for them to understand
what the program does. Remember, you could be that person yourself
in half a year!

'''

# эта функция проверяет является ли значение переменной целочисленным./this function checks if the value of the variable is an integer.
def check_num(num):

    if isinstance(num, int):
        print('Это число!')

    else:
        print('Это не число!')
