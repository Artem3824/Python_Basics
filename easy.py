# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

print('Задание - 1')


# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def person(name, age, city):
    result = f'{name}, {age} год(а), проживает в городе {city}'
    return result


print(person('Артем', 28, 'Москва'))

print('C помощью lambda:')
person_info = lambda name, age, city: f'{name}, {age} год(а), проживает в городе {city}'
print(person_info('Артем', 28, 'Москва'))

print()
print('Задание - 2')


# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def number(a, b, c):
    return max(a, b, c)


print(number(25, 50, 77))

print('C помощью lambda:')
result = lambda a, b, c: max(a, b, c)
print(result(25, 50, 77))

print()
print('Задание - 3')


# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def long_string(*args):
    strings = list(sorted(args, key=lambda x: len(x), reverse=True))
    return strings[0]


print(long_string('Светлана', 'Анастасия', 'Тамара', 'Ирина', 'Севастополь'))
