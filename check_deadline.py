'''
    Grade 1. Этап 2. Задание 3
    Задание: Обработка дедлайнов
    Сравнивает дату дедлайна заметки (issue_date) с текущей датой.
    Выводит соответствующее сообщение:
    Если дедлайн истёк, предупреждает пользователя.
    Если дедлайн не истёк, сообщает, сколько времени осталось до истечения срока.
'''

# Подключение модуля для работы с датами
from datetime import datetime

# Создание списка для хранения данных об заметке
list_info = [
    "Имя пользователя", "Содержание заметки",
    "Статус заметки", "Дата создания заметки",
    "Дата изменения заметки", ["Заголовок 1", "Заголовок 2", "Заголовок 3"]
]

# Ввод данных об заметке
print('Ввод информации об заметке:')
username = input('Введите имя пользователя: ')
content = input('Введите содержание заметки: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания заметки в формате "ДД-ММ-ГГГГ": ')
edit_date = input('Введите дату изменения заметки в формате "ДД-ММ-ГГГГ": ')

list_title = []  # Создание пустово списка для хранения заголовков заметки

# Ввод заголовков заметки с помощью цикла
while True:
    title_input = input('Введите заголовок заметки (введите "стоп" или оставьте пустым для завершения ввода): ')

    # удаление возможных пробелов в начале и в конце
    title = title_input.strip()

    # если введено пустое значение либо слово 'стоп', то выходим из цикла
    if title == '' or title.lower() == 'стоп':
        break
    else:
        # проверка на уникальность заголовка
        if list_title.count(title) == 0:
            list_title.append(title)
        else:
            print('Заголовок заметки \"' + title + "\" уже есть в списке!")

# Ввод даты истечения заметки (дедлайн)
while True:
    issue_date = input('Введите дату истечения заметки (дедлайн) в формате "ДД-ММ-ГГГГ" либо "ГГГГ-ММ-ДД": ')

    # проверка на введенной даты на корректность
    try:
        valid_date = datetime.strptime(issue_date, '%d-%m-%Y')
        break
    except ValueError:
        try:
           valid_date = datetime.strptime(issue_date, '%Y-%m-%d')

           # Приводим введенную дату к формату ДД-ММ-ГГГГ
           issue_date = valid_date.strftime('%d-%m-%Y')

           break
        except ValueError:
           print('Дата введена некорректно!')

# Создание списка с данными об заметке
list_info = [username, content, status, created_date, edit_date, list_title, issue_date]

# Изменение статуса заметки
print()
print('Текущий статус заметки: ' + list_info[2])
while True:
    new_status = input("""Выберите новый статус заметки:
1 выполнено
2 в процессе
3 отложено
> """)

    # Обработка введенного значения

    # удаление возможных пробелов в начале и в конце
    new_status = new_status.strip()

    # если введенное значение состоит из букв
    if new_status.isalpha():
        if new_status == 'выполнено' or new_status == 'в процессе' or new_status == 'отложено':
            break
        else:
            print('Введено некорректное значение статуса!')

    # если введенное значение состоит из цифр
    elif new_status.isdigit():
        if new_status == '1':
            new_status = 'выполнено'
            break
        elif new_status == '2':
            new_status = 'в процессе'
            break
        elif new_status == '3':
            new_status = 'отложено'
            break
        else:
            print('Введено некорректное значение статуса!')
    else:
       print('Введено некорректное значение статуса!')

 # Если статус был изменен, то изменяем его значение в данных
if list_info[2] != new_status:
    list_info[2] = new_status
    print('Установлен новый статус заметки: ' + list_info[2])

# Вывод данных заметки на экран
print()
print('Информация об заметке: ')
print("Имя пользователя: " + list_info[0])
print("Содержание заметки: " + list_info[1])
print("Статус заметки: " + list_info[2])
print("Дата создания: " + list_info[3][:-5])
print("Дата изменения: " + list_info[4][:-5])

# Вывод данных об истечения заметки (дедлайн) на экран

# Если дата меньше текущей
if datetime.strptime(list_info[6], '%d-%m-%Y').date() < datetime.today().date():
    print('Внимание, дедлайн истёк: '+list_info[6]+'!')
elif datetime.strptime(list_info[6], '%d-%m-%Y').date() == datetime.today().date():
    print('Внимание, дедлайн истекает сегодня!')
else:
    delta = datetime.strptime(list_info[6], '%d-%m-%Y') - datetime.today()
    print('До истечения срока дедлайн осталось дней: ', delta.days)

# Проверка на пустой список заголовков заметок
if len(list_info[5]) == 0:
    print('Заголовки заметки не введены')
else:
    # Вывод заголовков заметки
    print('Заголовки заметки:')
    i = 0
    while i != len(list_info[5]):
        print(str(i + 1) + ': ' + list_info[5][i])
        i += 1
