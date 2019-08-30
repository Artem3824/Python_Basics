# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

from easy import create_folder, delete_folder, content_folder, change_path

import os
import sys

try:
    command = sys.argv[1]
except IndexError:
    print('Введите команду help, чтобы открыть список возможных команд')
else:
    if command == 'help':
        print('Воспользуйтесь данными командами для выполнения действий:')
        print('1. move - перейти в папку')
        print('2. content - просмотреть содержимое текущей папки')
        print('3. delete - удалить папку')
        print('4. create - создать папку')
    elif command == 'content':
        content_folder()
    elif command == 'move':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует наименование папки')
        else:
            change_path(name)
    elif command == 'create':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует наименование папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует наименование папки')
        else:
            delete_folder(name)


# create_folder('dir1')
# delete_folder('dir1')
# content_folder()
# os.getcwd()
# change_path('dir')
# print(os.getcwd())
