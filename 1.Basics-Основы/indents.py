'''
-----------------------------------------------RU----------------------------------------------------------------
В Python пробелы важны. Точнее, пробелы в начале строки важны.
Это называется отступами. Отступы (пробелы и *табуляции)
в начале строки используются для определения уровня отступа логической строки.
Это означает, что кусочки кода, идущие вместе, должны иметь одинаковый отступ.
Каждый такой набор кусочков кода называется блоком. Вы должны запомнить,
что неправильные отступы могут приводить к возникновению ошибок.

Не смешивайте пробелы и символы *табуляции в одном коде,
поскольку не во всех редакторах это работает корректно.
Я настоятельно рекомендую вам использовать одинарную
*табуляцию или четыре пробела для каждого уровня отступа.
Выберите какой-нибудь один из этих стилей отступа.
Но что ещё более важно, это использовать выбранный стиль постоянно,
а также соблюдать стиль редактируемых вами файлов. Т.е. когда вы пишете новый файл,
используйте только один ваш любимый стиль, а если в редактируемом вами файле
для отступов уже используются, скажем, символы *табуляции, то и вы используйте
в этом файле символы *табуляции для отступов.

Indentation lives matter!

*Табуляция - нажатие на кнопку Tab

------------------------------------------------EN---------------------------------------------------------------
In Python, spaces are important. More precisely, spaces at the beginning of a line are important.
These are called indents. Indentations (spaces and tabs)
at the beginning of a line are used to determine the indentation level of a logical string.
This means that pieces of code going together must have the same indentation.
Each such set of pieces of code is called a block. You must remember that improper indentation
can cause errors.

Do not mix spaces and *tabulation characters in the same code,
because this does not work correctly in all editors.
I strongly recommend that you use a single
*tabulation or four spaces for each indentation level.
Choose any one of these indentation styles.
But what's even more important is to use the style you choose at all times,
and also to respect the style of the files you're editing. That is, when you write a new file,
use only one of your favorite styles, and if the file you're editing
is already using, say, *tabulation characters for indents, then you use
*tabulation characters for indentation in that file.

Indentation matters!

*Tabulation - pressing the Tab button

Indentation lives matter!

'''

i = 5
 print('Значение составляет ', i) # Alert! Пробел в начале строки/Space at the beginning of the line
print('Я повторяю, значение составляет ', i)


'''
Результат работы программы:

File "indents.py", line 23
print('Значение составляет ', i) # Alert! Пробел в начале строки
^
IndentationError: unexpected indent

The result of the program:

File "indents.py", line 23
print('The value is ', i) # Alert! Space at the beginning of the line
^
IndentationError: unexpected indent

'''

# py indents.py - запуск файла/file run

# i - названия переменных/variable name

# print() - название функции. Названия функций обязательно записываются со скобками/function name.
#Function names must be written with parentheses
