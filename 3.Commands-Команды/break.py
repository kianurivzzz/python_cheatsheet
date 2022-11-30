'''
-----------------------------------------------RU----------------------------------------------------------------
Команда break служит для прерывания цикла, т.е. остановки выполнения команд даже
если условие выполнения цикла ещё не приняло значения False или
последовательность элементов не закончилась.
Важно отметить, что если циклы for или while прервать командой break,
соответствующие им блоки else выполняться не будут.


------------------------------------------------EN---------------------------------------------------------------
Command break operator is used to interrupt the loop,
i.e. to stop the execution of commands even if the
even if the loop's condition has not yet become False, or
or if the sequence of elements has not been terminated.
It is important to note that if the for or while loops are interrupted by the break command,
the corresponding else blocks will not be executed.

'''

while True:
    s = input('Введите что-нибудь : ')

    if s == 'выход':
        break # останавливает цикл, если пользователь ввёл слово 'выход'

    print('Длина строки:', len(s))

print('Завершение')

# # py break.py - запуск файла/file run
