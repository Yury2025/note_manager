'''
    Grade 1. Этап 2. Задание 4
    Задание: Работа с несколькими заметками
    Напишите программу, которая позволяет пользователю:
    1. Создавать несколько заметок, каждая из которых хранится в виде словаря.
       Реализуйте цикл, который позволяет пользователю добавлять любое количество заметок.
       Предусмотрите возможность завершения ввода новых заметок
       (например, с помощью команды "стоп").
    2. Добавлять заметки в список для их упорядоченного хранения.
    3. Выводить список всех созданных заметок с понятным форматированием.
'''

# Подключение модуля для работы с датами
from datetime import datetime

# Проверка даты на соответствие формату и значение не менее min_data
def data_check(value_data, min_data='01-01-0001'):
    min_data_check = datetime.strptime(min_data, '%d-%m-%Y')
    try:
        valid_date = datetime.strptime(value_data, '%d-%m-%Y')
        if datetime.strptime(value_data, '%d-%m-%Y').date() < min_data_check.date():
            print('Введенная дата не может быть меньше даты ' + min_data + '!')
            return False
        else:
            return True

    except ValueError:
        try:
            valid_date = datetime.strptime(value_data, '%Y-%m-%d')

            # Приводим введенную дату к формату ДД-ММ-ГГГГ
            value_data = valid_date.strftime('%d-%m-%Y')

            if datetime.strptime(value_data, '%d-%m-%Y').date() < min_data_check.date():
                print('Введенная дата не может быть меньше даты ' + min_data + '!')
                return False
            else:
                return value_data

        except ValueError:
            print('Дата введена некорректно!')
            return False

# Ввод символьного значения с проверкой
def text_input(Title):
    while True:
        value_input = input(Title)

        if value_input.strip() == '':
            print('Введено пустое значение!')

    return value_input

# Создание списка для хранения данных об заметках
notes = []

# Ввод данных об заметке
break_all = False
while True:
    print()
    print('Ввод информации об заметке:')

        username = text_input('Введите имя пользователя: ')
        content = text_input('Введите содержание заметки: ')

     # Ввод статуса заметки с проверкой
    while True:
        status = text_input("""Выберите статус заметки:
1 выполнено
2 в процессе
3 отложено
> """)

        # Обработка введенного значения
        # удаление возможных пробелов в начале и в конце
        status = status.strip()

        # если введенное значение состоит из букв
        if status.isalpha():
            status = status.lower()
            if status == 'выполнено' or status == 'в процессе' or status == 'отложено':
                break
            else:
                print('Введено некорректное значение статуса!')

        # если введенное значение состоит из цифр
        elif status.isdigit():
            if status == '1':
                status = 'выполнено'
                break
            elif status == '2':
                status = 'в процессе'
                break
            elif status == '3':
                status = 'отложено'
                break
            else:
                print('Введено некорректное значение статуса!')
        else:
            print('Введено некорректное значение статуса!')

    # Ввод даты создания заметки с проверкой
    print()
    while True:
        created_date = input('Введите дату создания заметки в формате "ДД-ММ-ГГГГ" либо "ГГГГ-ММ-ДД": ')

        # проверка введенной даты на корректность
        result = data_check(created_date)
        if type(result) == bool:
            if result:
                break
        else:
            created_date = result

    # Ввод даты изменения заметки с проверкой
    while True:
        edit_date = input('Введите дату изменения заметки в формате "ДД-ММ-ГГГГ" либо "ГГГГ-ММ-ДД": ')

        # проверка введенной даты на корректность
        result = data_check(edit_date, created_date)
        if type(result) == bool:
            if result:
                break
        else:
            edit_date = result
            break

    # Создание списка для хранения заголовков заметки
    list_title = []

    # Ввод заголовков заметки с помощью цикла
    print()
    print('Ввод заголовков')
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

    # Ввод даты истечения заметки (дедлайн) с проверкой
    print()
    while True:
        issue_date = input('Введите дату истечения заметки (дедлайн) в формате "ДД-ММ-ГГГГ" либо "ГГГГ-ММ-ДД": ')

        # проверка введенной даты на корректность
        result = data_check(issue_date, created_date)
        if type(result) == bool:
            if result:
                break
        else:
            issue_date = result
            break

    # Создание словаря с данными об заметке
    note = {'Пользователь': username,
            'Заголовки': list_title,
            'Содержание': content,
            'Статус': status,
            'Дата создания': created_date,
            'Дата изменения': edit_date,
            'Дата дедлайн': issue_date}

    # Добавления в список заметок новой записи
    notes.append(note)

    # Спросим о добавлении новой заметки, либо заверешении
    print()
    while True:
        answer = input('Хотите добавить новую заметку (да/нет): ')
        answer = answer.strip()
        if answer.lower() == 'нет':
            # Устанавливаем значение 'флага' прекращения цикла добавления заметок в True
            break_all = True
            break
        elif answer.lower() == 'да':
            break
        else:
            print('Ответ непонятен!')

    # Прекращение цикла добавления заметок
    if break_all:
        break

# Вывод данных об заметках на экран
print('Информация об заметках:')
i = 0
while i != len(notes):
    print()
    print('Заметка ' + str(i + 1) + ':')
    print("Имя пользователя: ", notes[i]['Пользователь'])
    print("Содержание заметки: ", notes[i]['Содержание'])
    print("Статус заметки: ", notes[i]['Статус'])
    print("Дата создания: ", notes[i]['Дата создания'][:-5])
    print("Дата изменения: ", notes[i]['Дата изменения'][:-5])
    print("Дата дедлайна: ", notes[i]['Дата дедлайн'][:-5], end='  ')

    # Вывод данных об истечения заметки (дедлайн) на экран
    if datetime.strptime(notes[i]['Дата дедлайн'], '%d-%m-%Y').date() < datetime.today().date():
        print('Внимание, дедлайн истёк: ' + notes[i]['Дата дедлайн'] + '!')
    elif datetime.strptime(notes[i]['Дата дедлайн'], '%d-%m-%Y').date() == datetime.today().date():
        print('Внимание, дедлайн истекает сегодня!')
    else:
        delta = datetime.strptime(notes[i]['Дата дедлайн'], '%d-%m-%Y') - datetime.today()
        print('До истечения срока дедлайн осталось дней: ', delta.days)

    # Вывод данных об заголовках
    # Проверка на пустой список заголовков заметок
    if len(notes[i]['Заголовки']) == 0:
        print('Заголовки заметки не введены')
    else:
        # Вывод заголовков заметки
        j = 0
        while j != len(notes[i]['Заголовки']):
            print('Заголовок ' + str(j  + 1) + ': ' + notes[i]['Заголовки'][j])
            j += 1

    i += 1

# Запоминаем текущее количество заметок
quantity_notes = len(notes)

# Спросим об удалении заметки
print()
break_all = False
while True:
    answer = input('Хотите удалить заметку (да/нет): ')

    answer = answer.strip()

    if answer.lower() == 'нет':
        break

    elif answer.lower() == 'да':
        # Если 'да', то просим указать номер удаляемой заметки
        while True:
            number = input('Укажите номер удаляемой заметки, либо пустое значения для отказа')
            number = number.strip()

            # если введенное значение состоит из цифр
            if number.isdigit():
                id = int(number)
                if len(notes) < id:
                    print('Введено некорректное значение, в списке имеется '+str(len(notes))+' заметок!')
                else:
                    print('Удалена  '+str(id)+' заметка!')
                    notes.pop(id-1)
                    break_all = True
                    break

            elif number == '':
                break_all = True
                break

            else:
                print('Введено некорректное значение!')

    else:
        print('Ответ непонятен!')

    # Прекращение цикла удаления заметок
    if break_all:
        break

# Если количество заметок изменилось, то повторно выводим их
if quantity_notes != len(notes):
    # Вывод данных об заметках на экран
    print('Информация об заметках:')
    i = 0
    while i != len(notes):
        print()
        print('Заметка ' + str(i + 1) + ':')
        print("Имя пользователя: ", notes[i]['Пользователь'])
        print("Содержание заметки: ", notes[i]['Содержание'])
        print("Статус заметки: ", notes[i]['Статус'])
        print("Дата создания: ", notes[i]['Дата создания'][:-5])
        print("Дата изменения: ", notes[i]['Дата изменения'][:-5])
        print("Дата дедлайна: ", notes[i]['Дата дедлайн'][:-5], end='  ')

        # Вывод данных об истечения заметки (дедлайн) на экран
        if datetime.strptime(notes[i]['Дата дедлайн'], '%d-%m-%Y').date() < datetime.today().date():
            print('Внимание, дедлайн истёк: ' + notes[i]['Дата дедлайн'] + '!')
        elif datetime.strptime(notes[i]['Дата дедлайн'], '%d-%m-%Y').date() == datetime.today().date():
            print('Внимание, дедлайн истекает сегодня!')
        else:
            delta = datetime.strptime(notes[i]['Дата дедлайн'], '%d-%m-%Y') - datetime.today()
            print('До истечения срока дедлайн осталось дней: ', delta.days)

        # Вывод данных об заголовках
        # Проверка на пустой список заголовков заметок
        if len(notes[i]['Заголовки']) == 0:
            print('Заголовки заметки не введены')
        else:
            # Вывод заголовков заметки
            j = 0
            while j != len(notes[i]['Заголовки']):
                print('Заголовок ' + str(j  + 1) + ': ' + notes[i]['Заголовки'][j])
                j += 1

        i += 1
