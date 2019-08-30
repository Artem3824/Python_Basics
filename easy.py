# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

#cоздание папок
def new_folders():
    for i in range(1,10):
        os.mkdir(f'dir_{i}')

#удаление папок
def delete_folders():
    for i in range(1, 10):
        os.rmdir(f'dir_{i}')

#cоздание одной папки с названием
def create_folder(name):
    try:
        os.mkdir(name)
        print(f'Папка "{name}" успешно создана')
    except FileExistsError:
        print('Невозможно создать папку. Папка с таким названием уже существует')

#удаление одной папки с названием
def delete_folder(name):
    os.rmdir(name)
    print(f'Папка {name} успешно удалена')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

#просмотр содержимого текущей папки
def content_folder():
    print(os.listdir())

#просмотр содержимого, только папки
def folders_only():
    result = os.listdir()
    result = [folder for folder in result if os.path.isdir(folder)]
    print(result)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
def copy_file(name, new_name):
    shutil.copy(name, new_name)

#переход в папку

def change_path(name):
    try:
        os.chdir(name)
    except FileNotFoundError:
        print('Такой папки не существует')
    else:
        print(f'Произведен переход в папку {name}')
        print(os.getcwd())




# if __name__ == '__main__':
#     new_folders()
#     delete_folders()
#     folders_only()
#     copy_file('easy.py', 'easy_3.py')
#     create_folder('folder1')
#     delete_folder('folder1')
#     content_folder()
#     change_path('dir')
#     print(os.getcwd())