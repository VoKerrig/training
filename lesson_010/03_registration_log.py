# -*- coding: utf-8 -*-
from pprint import pprint
from random import randint
from termcolor import cprint

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код


class CustomException(Exception):
    def __init__(self, message=None):
        if message:
            self.message = message

        super(Exception, self).__init__(self.message)


class NotNameError(CustomException):
    message = 'Поле имени содержит НЕ только буквы'


class NotEmailError(CustomException):
    message = 'Поле емейл НЕ содержит @ и .'


def check(line):
    row = line.split(' ')
    if len(row) != 3 or not all(row):
        raise ValueError('НЕ присутсвуют все три поля')

    name, email, age = row
    if not age.isdigit() or int(age) not in range(10, 100):
        raise ValueError(f'Поле возраст НЕ является числом от 10 до 99, {age}')

    elif not str.isalpha(name):
        raise NotNameError
    elif '@' and '.' not in email:
        raise NotEmailError
    return name, email, age


with open('registrations.txt', mode='r', encoding='utf8') as file:
    for line in file:
        line = line[:-1]
        try:
            check(line)
            with open('registrations_good_log.txt', 'a', encoding='utf8') as file_good:
                file_good.write(line + '\n')

        except (ValueError, NotNameError, NotEmailError) as exc:
            with open('registrations_bad_log.txt', 'a', encoding='utf8') as file_bad:
                file_bad.write(line + '\n')
            cprint(f'{exc}, в строке {line}', color='red')
