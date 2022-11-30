'''
-----------------------------------------------RU----------------------------------------------------------------
Здесь перечислены встроенные в Python функции, которые нужно знать.
Список будет расширяться.


abs(x) - Возвращает абсолютную величину (модуль числа).

all(последовательность) - Возвращает True, если все элементы истинные (или, если последовательность пуста).

any(последовательность) - Возвращает True, если хотя бы один элемент - истина. Для пустой последовательности возвращает False.

ascii(object) - Как repr(), возвращает строку, содержащую представление объекта, но заменяет не-ASCII символы на экранированные последовательности.

bin(x) - Преобразование целого числа в двоичную строку.

callable(x) - Возвращает True для объекта, поддерживающего вызов (как функции).

chr(x) - Возвращает односимвольную строку, код символа которой равен x.

classmethod(x) - Представляет указанную функцию методом класса.

compile(source, filename, mode, flags=0, dont_inherit=False) - Компиляция в программный код, который впоследствии может выполниться функцией eval или exec. Строка не должна содержать символов возврата каретки или нулевые байты.

delattr(object, name) - Удаляет атрибут с именем 'name'.

dir([object]) - Список имен объекта, а если объект не указан, список имен в текущей локальной области видимости.

divmod(a, b) - Возвращает частное и остаток от деления a на b.

enumerate(iterable, start=0) - Возвращает итератор, при каждом проходе предоставляющем кортеж из номера и соответствующего члена последовательности.

eval(expression, globals=None, locals=None) - Выполняет строку программного кода.

exec(object[, globals[, locals]]) - Выполняет программный код на Python.

filter(function, iterable) - Возвращает итератор из тех элементов, для которых function возвращает истину.

format(value[,format_spec]) - Форматирование (обычно форматирование строки).

getattr(object, name ,[default]) - извлекает атрибут объекта или default.

globals() - Словарь глобальных имен.

hasattr(object, name) - Имеет ли объект атрибут с именем 'name'.

hash(x) - Возвращает хеш указанного объекта.

help([object]) - Вызов встроенной справочной системы.

hex(х) - Преобразование целого числа в шестнадцатеричную строку.

id(object) - Возвращает "адрес" объекта. Это целое число, которое гарантированно будет уникальным и постоянным для данного объекта в течение срока его существования.

input([prompt]) - Возвращает введенную пользователем строку. Prompt - подсказка пользователю.

isinstance(object, ClassInfo) - Истина, если объект является экземпляром ClassInfo или его подклассом. Если объект не является объектом данного типа, функция всегда возвращает ложь.

issubclass(класс, ClassInfo) - Истина, если класс является подклассом ClassInfo. Класс считается подклассом себя.

iter(x) - Возвращает объект итератора.

len(x) - Возвращает число элементов в указанном объекте.

locals() - Словарь локальных имен.

map(function, iterator) - Итератор, получившийся после применения к каждому элементу последовательности функции function.

max(iter, [args ...] * [, key]) - Максимальный элемент последовательности.

min(iter, [args ...] * [, key]) - Минимальный элемент последовательности.

next(x) - Возвращает следующий элемент итератора.

oct(х) - Преобразование целого числа в восьмеричную строку.

open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True) - Открывает файл и возвращает соответствующий поток.

ord(с) - Код символа.

pow(x, y[, r]) - ( x ** y ) % r.

reversed(object) - Итератор из развернутого объекта.

repr(obj) - Представление объекта.

print([object, ...], *, sep=" ", end='\n', file=sys.stdout) - Печать.

property(fget=None, fset=None, fdel=None, doc=None)

round(X [, N]) - Округление до N знаков после запятой.

setattr(объект, имя, значение) - Устанавливает атрибут объекта.

sorted(iterable[, key][, reverse]) - Отсортированный список.

staticmethod(function) - Статический метод для функции.

sum(iter, start=0) - Сумма членов последовательности.

super([тип [, объект или тип]]) - Доступ к родительскому классу.

type(object) - Возвращает тип объекта.

type(name, bases, dict) - Возвращает новый экземпляр класса name.

vars([object]) - Словарь из атрибутов объекта. По умолчанию - словарь локальных имен.

zip(*iters) - Итератор, возвращающий кортежи, состоящие из соответствующих элементов аргументов-последовательностей.

------------------------------------------------EN---------------------------------------------------------------
Here are the built-in Python functions you need to know.
The list will be expanded.


abs(x) - Returns an absolute value (the modulus of a number).

all(sequence) - Returns True if all elements are true (or if the sequence is empty).

any(sequence) - Returns True if at least one element is true. For an empty sequence it returns False.

ascii(object) - Like repr(), returns a string containing the representation of the object, but replaces non-ASCII characters with escaped sequences.

bin(x) - Converts an integer to a binary string.

callable(x) - Returns True for a callable object (as a function).

chr(x) - Returns a one-character string whose character code is x.

classmethod(x) - Represents the specified function as a class method.

compile(source, filename, mode, flags=0, dont_inherit=False) - Compiles into program code that can be executed later by the eval or exec function. The string must not contain carriage return characters or null bytes.

delattr(object, name) - Deletes the attribute named 'name'.

dir([object]) - A list of object names, or if no object is specified, a list of names in the current local scope.

divmod(a, b) - Returns the quotient and remainder of a divided by b.

enumerate(iterable, start=0) - Returns an iterator that provides a tuple of the number and corresponding sequence member on each pass.

eval(expression, globals=None, locals=None) - Executes a line of program code.

exec(object[, globals[, locals]]) - Executes the program code in Python.

filter(function, iterable) - Returns an iterator of those elements for which function returns true.

format(value[,format_spec]) - Format (usually string formatting).

getattr(object, name ,[default]) - Retrieves object attribute or default.

globals() - The dictionary of global names.

hasattr(object, name) - Whether the object has an attribute named 'name'.

hash(x) - Returns the hash of the specified object.

help([object]) - Calls the built-in help system.

hex(x) - Converts an integer to a hex string.

id(object) - Returns the "address" of the object. This is an integer that is guaranteed to be unique and constant for the object during its lifetime.

input([prompt]) - Returns the string entered by the user. Prompt - A prompt to the user.

isinstance(object, ClassInfo) - True if the object is an instance of ClassInfo or its subclass. If the object is not an instance of that type, the function always returns false.

issubclass(class, ClassInfo) - True if the class is a subclass of ClassInfo. The class is considered a subclass of itself.

iter(x) - Returns the iterator object.

len(x) - Returns the number of elements in the specified object.

locals() - A dictionary of local names.

map(function, iterator) - The iterator obtained after applying a function to each element of the sequence.

max(iter, [args ...] * [, key]) - The maximal element of the sequence.

min(iter, [args ...] * [, key]) - The minimal element of the sequence.

next(x) - Returns the next element of the iterator.

oct(x) - Convert the integer to an octal string.

open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True) - Opens the file and returns the corresponding stream.

ord(c) - Character code.

pow(x, y[, r]) - ( x ** y ) % r.

reversed(object) - Iterates from the reversed object.

repr(obj) - Representation of the object.

print([object, ...], *, sep=" ", end='\n', file=sys.stdout) - Print.

property(fget=None, fset=None, fdel=None, doc=None)

round(X [, N]) - Rounding to N decimal places.

setattr(object, name, value) - Sets the attribute of the object.

sorted(iterable[, key][, reverse]) - Sorted list.

staticmethod(function) - Static method for the function.

sum(iter, start=0) - The sum of the members of the sequence.

super([type[, object or type]]) - Access to the parent class.

type(object) - Returns the type of the object.

type(name, bases, dict) - Returns a new instance of the name class.

vars([object]) - A dictionary of object attributes. Defaults to the local name dictionary.

zip(*iters) - Iterator that returns tuples consisting of the corresponding elements of the argument-sequences.

'''
