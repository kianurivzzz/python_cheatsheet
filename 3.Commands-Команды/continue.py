'''
-----------------------------------------------RU----------------------------------------------------------------
Команда continue используется для указания Python, что необходимо пропустить все
оставшиеся команды в текущем блоке цикла и продолжить
со следующей итерации цикла.


------------------------------------------------EN---------------------------------------------------------------
The continue command is used to tell Python to skip all
remaining commands in the current loop block and continue
with the next iteration of the loop.

'''


while True:
    s = input('Введите что-нибудь : ')

    if s == 'выход':
        break
    elif len(s) < 3:
        print('Слишком мало')
        continue

print('Введённая строка достаточной длины')
# Другие действия здесь...

# py continue.py - запуск файла/file run
