# Эти задачи необходимо решить используя регулярные выражения!

print('Задание-1:')
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.


import re

name = input('Введите Ваше имя: ')
surname = input('Введите Вашу фамилию: ')
email = input('Введите Ваш email: ')
pattern = r'\b[A-Z|А-Я]\w+'
pattern2 = r'[a-z0-9_]+@[a-z0-9]+\.(ru|org|com)'
found_name = re.match(pattern, name)
found_surname = re.match(pattern, surname)
found_mail = re.match(pattern2, email)

while True:
    if found_name is None:
        print('Неверно указано имя. Введите имя с заглавной буквы!')
        name = input('Введите Ваше имя: ')
        found_name = re.match(pattern, name)
    elif found_surname is None:
        print('Неверно указана фамилия. Введите фамилию с заглавной буквы')
        surname = input('Введите Вашу фамилию: ')
        found_surname = re.match(pattern, surname)
    elif found_mail is None:
        print('Неверно указан Email')
        email = input('Введите Вашу фамилию: ')
        found_mail = re.match(pattern2, email)
    else:
        print('Ваши данные введены корректно!')
        break


print()
print('Задание-2:')
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

pattern3 = r'\...\W'
comma = re.findall(pattern3, some_str)
print('В данном тексте есть троеточие!' if comma else 'Троеточия не нашлось')