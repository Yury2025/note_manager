'''
    Grade 1. Этап 2. Задание 5
    Задание: Удаление заметок
    Напишите программу, которая предоставляет пользователю возможность удалить заметку
    из списка заметок.
    Программа должна:
    1. Запрашивать у пользователя критерий для удаления (например, имя пользователя
       или заголовок).
    2. Удалять все заметки, соответствующие введённому критерию.
    3. Если заметок для удаления не найдено, выводить соответствующее сообщение.
    4. После удаления оставлять остальные заметки в списке.
'''

# Подключение модуля для работы с датами
from datetime import datetime

# Удаление заметок
def del_note(find_value):

    # Определение номеров удаляемых заметок
    id_del_notes = []
    str_id_del_notes = ''
    for i, note in enumerate(notes):
        # Поиск в имени пользователя
        if note['Пользователь'].lower().find(find_value.strip().lower()) != -1:
            id_del_notes.append(i)
            str_id_del_notes = str_id_del_notes + ', ' + str(i+1)
        else:
            # Поиск в заголовках
            j = 0
            while j != len(note['Заголовки']):
                if note['Заголовки'][j].lower().find(find_value.strip().lower()) != -1:
                    id_del_notes.append(i)
                    str_id_del_notes = str_id_del_notes + ', ' + str(i+1)
                    break
                j += 1

    # Если ничего не найдено
    if len(id_del_notes) == 0:
        print('По заданному значению никаких заметок не найдено!')
    else:
        # Уточняем, что хотим удалить найденные заметки
        str_id_del_notes = str_id_del_notes[2:]
        while True:
            answer = input('Вы действительно Хотите удалить заметки: '+str_id_del_notes+' (да/нет)?: ')
            answer = answer.strip()

            if answer.lower() == 'да':
                # Удаляем найденные заметки, начиная с конца списка
                for i in range(0, len(id_del_notes)):
                    index = (len(id_del_notes) - 1) - i
                    notes.pop(id_del_notes[index])

                return False
            elif answer.lower() == 'нет':
                return False
            else:
                print('Ответ непонятен!')

# Вывод данных об заметках на экран
def print_notes(notes):
    print()
    print('Текущие заметки:')
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
                print('Заголовок ' + str(j + 1) + ': ' + notes[i]['Заголовки'][j])
                j += 1

        i += 1

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
        else:
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
print_notes(notes)

# Запоминаем текущее количество заметок
quantity_notes = len(notes)

break_all = False
while True:

    # Если количество заметок изменилось, то повторно выводим их
    if quantity_notes != len(notes):
        quantity_notes = len(notes)
        # Вывод данных об заметках на экран
        print_notes(notes)

    print()
    while True:
        answer = text_input('Введите имя пользователя или заголовок для удаления заметки,'
                            +' либо "стоп" для остановки удаления: ')

        answer = answer.strip()

        if answer.lower() == 'стоп':
            break_all = True
            break

        else:
            del_note(answer)
            break

    # Прекращение цикла удаления заметок
    if break_all:
        break
