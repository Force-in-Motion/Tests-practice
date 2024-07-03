def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError('Получен не верный тип данных, ожидалась строка')

    if len(s) < 2:
        raise ValueError('Строка, имеющая меньше 2 символов не может быть палиндромом')

    return s == s[::-1]

