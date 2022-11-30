'''
-----------------------------------------------RU----------------------------------------------------------------
Условные операторы:

Оператор if используется для проверки условий: если (if) условие верно(например, a < b)
, тогда (:) выполняется один блок кода, иначе если (elif) выполняется другой блок выражений,
в противном случае (else) выполяется оставшийся блок. Порядок важен.
Первым всегда записывается if, потом (если это требуется) записываются elif или else.
Else всегда последний и не имеет условий.
Блоки elif и else являются необязательнымы.


------------------------------------------------EN---------------------------------------------------------------
Conditional operators:

The if statement is used to check conditions: if the condition is true (for example, a < b)
then (:) one block of code is executed, else if another block of expressions is executed,
else executes the rest of the block. The order is important.
The first is always written if, then (if needed) elif or else.
Else is always last and has no conditions.
The elif and else blocks are optional.

'''

number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('Поздравляю, вы угадали,') # Начало нового блока
    print('хоть и не выиграли никакого приза!') # Конец нового блока
elif guess < number:
    print('Нет, загаданное число немного больше этого.') # Ещё один блок
    # Внутри блока вы можете выполнять всё, что угодно ...
else:
    print('Нет, загаданное число немного меньше этого.')
    # чтобы попасть сюда, guess должно быть больше, чем number

# py if_elif_else.py - запуск файла/file run
