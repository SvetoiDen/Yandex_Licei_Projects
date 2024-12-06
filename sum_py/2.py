# Напишите функцию для выбора тех, кто уже счастлив.
# Функция wish() принимает произвольное количество строк и именованный аргумент n. Функция возвращает список отобранных строк (в исходном порядке):
#
# - выбираются строки, длина которых кратна числу n;

# - в них не должно быть посторонних символов кроме букв и, возможно, апострофа (одиночной кавычки);

# - хотя бы одна буква встречается в разных регистрах.

# Если строки не переданы, нужно возбудить собственное исключение EmptyInputError с сообщением “No input arguments”;
# если хотя бы один из позиционных аргументов – не строка, нужно возбудить стандартное исключение TypeError с сообщением “The argument is not a string”;
# если число отрицательное или ноль, нужно возбудить собственное исключение NegativeNumberError с сообщением “Negative or null argument”.
#
# Приоритет проверки исключений должен соответствовать порядку описания в задаче. Исключения нужно только порождать, перехватывать их будет тестирующая система!

class NegativeNumberError(Exception):
    pass


class EmptyInputError(Exception):
    pass


def wish(*args, n):
    list_answer = []
    if len(args) == 0:
        raise EmptyInputError('No input arguments')
    if n <= 0:
        raise NegativeNumberError("Negative or null argument")
    for arg in args:
        if isinstance(arg, str):
            pass
        else:
            raise TypeError('The argument is not a string')
        d1 = arg.split()
        for row in d1:
            if len(row) % n == 0:
                if row.isalpha() or row.count("'") > 0:

                    i = 0
                    for r in row:
                        if r.isupper():
                            i += 1
                    if i > 0:
                        list_answer.append(row)

    return list_answer
