'''
    Grade 1. Этап 3. Задание 2
    Функция обновления заметки.
    Напишите функцию, которая:
    1. Принимает заметку (словарь) в качестве аргумента.
    2. Позволяет пользователю выбрать, какое поле заметки нужно обновить.
    3. Запрашивает новое значение для выбранного поля.
    4. Обновляет указанное поле заметки.

    Реализуйте проверку корректности формата для поля issue_date
    (например, "день-месяц-год").
'''

# Подключение модуля для работы с датами
from datetime import datetime

# Удаление заметок по заданному критерию
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
        return False
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

                return True
            elif answer.lower() == 'нет':
                return False
            else:
                print('Ответ непонятен!')

# Удаление заметок
def del_notes():
    if len(notes) == 0:
        print('Список заметок пуст!')
        return False

    while True:
        answer = text_input('Введите имя пользователя или заголовок для удаления заметки,'
                            +' либо "стоп" для остановки удаления: ')

        answer = answer.strip()

        if answer.lower() == 'стоп':
            return False
        else:
            return del_note(answer)

# Вывод данных об заметках на экран
def print_notes(notes):
    print()
    print('Текущие заметки:')
    i = 0
    while i != len(notes):
        print()
        print('Заметка ' + str(i + 1) + ':')
        print("Имя пользователя: ", notes[i]['Пользователь'])
        print("Описание заметки: ", notes[i]['Описание'])
        print("Статус заметки: ", notes[i]['Статус'])
        print("Дата создания: ", notes[i]['Дата создания'][:-5])
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


# Ввод статуса заметки с проверкой
def status_input(Title):
    while True:
        print(Title, end='')
        status = text_input("""
1 новая
2 в процессе
3 выполнена
> """)

        # Обработка введенного значения
        # Удаление возможных пробелов в начале и в конце
        status = status.strip()

        # Если введенное значение состоит из букв
        if status.isalpha():
            status = status.lower()
            if status == 'новая' or status == 'в процессе' or status == 'выполнена':
                break
            else:
                print('Введено некорректное значение статуса!')

        # Если введенное значение состоит из цифр
        elif status.isdigit():
            if status == '1':
                status = 'новая'
                break
            elif status == '2':
                status = 'в процессе'
                break
            elif status == '3':
                status = 'выполнена'
                break
            else:
                print('Введено некорректное значение статуса!')
        else:
            print('Введено некорректное значение статуса!')

    return status

# Создание новой заметки
def create_note():
    print()
    print('Ввод информации об заметке:')

    username = text_input('Введите имя пользователя: ')
    content = text_input('Введите описание заметки: ')
    status = status_input('Введите статус заметки:')

    # Автоматическое заполнение текщей датой
    created_date = datetime.today().date().strftime('%d-%m-%Y')

    # Ввод заголовков заметки с помощью цикла
    # Создание списка для хранения заголовков заметки
    list_title = []

    print()
    print('Ввод заголовков')
    while True:
        title_input = input('Введите заголовок заметки (введите "стоп" или оставьте пустым для завершения ввода): ')

        # Удаление возможных пробелов в начале и в конце
        title = title_input.strip()

        # Если введено пустое значение либо слово 'стоп', то выходим из цикла
        if title == '' or title.lower() == 'стоп':
            break
        else:
            # Проверка на уникальность заголовка
            if list_title.count(title) == 0:
                list_title.append(title)
            else:
                print('Заголовок заметки \"' + title + "\" уже есть в списке!")

    # Ввод даты истечения заметки (дедлайн) с проверкой
    print()
    while True:
        issue_date = input('Введите дату истечения заметки (дедлайн) в формате "ДД-ММ-ГГГГ" либо "ГГГГ-ММ-ДД": ')

        # Проверка введенной даты на корректность
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
            'Описание': content,
            'Статус': status,
            'Дата создания': created_date,
            'Дата дедлайн': issue_date}

    return note

# Обновления данных заметки
def update_note_title(list_title):
    print()
    print('Текущие заголовки:')
    # Вывод заголовков заметки
    j = 0
    while j != len(notes[i]['Заголовки']):
        print(str(j + 1) + ': ' + list_title[j])
        j += 1

    while True:
        answer = input('Введите обновляемый заголовок (оставьте пустым для отказа): ')
        answer = answer.strip()

        # Если введено пустое значение, то выходим из функции
        if answer == '':
            return list_title

        # Если введенное значение состоит из букв
        elif answer.isalpha():
            try:
                id = list_title.index(answer)
                break
            except ValueError:
                print('Такой заголовок не найден!')

        # Если введенное значение состоит из цифр
        elif answer.isdigit():
            try:
                number_ = int(answer)
                break
            except ValueError:
                print('Введено некорректное значение!')

            if number_ < 1 and number_ > 5:
                print('Введено некорректное значение!')
            else:
                id = answer
                break
        else:
            print('Введено некорректное значение!')

    title_input = text_input('Вместо "' + list_title[id-1]
                                  + '" введите новый заголовок: ')

    list_title[id-1] = title_input
    return list_title

# Обновления данных заметки
def update_note():
    if len(notes) == 0:
        print('Список заметок пуст!')
        return False

    # Ввод номера обновляемой заметки с проверкой
    while True:
        answer = input('Введите номер обновляемой заметки (оставьте пустым для отказа):')
        answer = answer.strip()

        # Если введено пустое значение, то выходим из функции
        if answer == '':
            return False

        elif answer.isdigit():
            try:
                number_note = int(answer)
                break
            except ValueError:
                print('Введено некорректное значение!')

            if number_note > len(notes):
                print('Введенный номер заметки больше имеющегося количества заметок!')
        else:
            print('Введено некорректное значение!')

        # Ввод обновляемого поля заметки с проверкой
        while True:
            answer = input("""Введите обновляемое поле заметки (оставьте пустым для отказа):
1 Пользователь
2 Заголовки
3 Описание
4 Статус
5 Дата дедлайн
> """)
            answer = answer.strip()

            # Если введено пустое значение, то выходим из функции
            if answer == '':
                return False

            # Если введенное значение состоит из букв
            elif answer.isalpha():
                answer = answer.lower()
                if (answer == 'пользователь'
                        or answer == 'заголовки'
                        or answer == 'описание'
                        or answer == 'статус'
                        or answer == 'дата дедлайн'):
                    answer = answer.title()
                    break
                else:
                    print('Введено некорректное значение статуса!')

            # Если введенное значение состоит из цифр
            elif answer.isdigit():
                try:
                    number_ = int(answer)
                    break
                except ValueError:
                    print('Введено некорректное значение!')

                if answer == '1':
                    answer = 'Пользователь'
                    break
                elif answer == '2':
                    answer = 'Заголовки'
                    break
                elif answer == '3':
                    answer = 'Описание'
                    break
                elif answer == '4':
                    answer = 'Статус'
                    break
                elif answer == '5':
                    answer = 'Дата дедлайн'
                    break
                else:
                    print('Введено некорректное значение!')
            else:
                print('Введено некорректное значение!')

        status = status_input()
        if answer == 'Пользователь':
            note['Пользователь'] = text_input('Вместо "'+note['Пользователь']
                                              +'" введите новое имя пользователя: ')
        elif answer == 'Описание':
            note['Описание'] = text_input('Вместо "' + note['Описание']
                                              + '" введите новое описание: ')
        elif answer == 'Заголовки':
            note['Заголовки'] = update_note_title(note['Заголовки'])

        elif answer == 'Статус':
            note['Статус'] = text_input('Вместо \"' + note['Статус']
                                              + '\" введите новый статус: ')
        elif answer == 'Дата дедлайн':
            while True:
                issue_date = input('Вместо "' + note['Дата дедлайн']
                                + '" введите новую дату дедлайн в формате "ДД-ММ-ГГГГ": ')

                # Проверка введенной даты на корректность
                result = data_check(issue_date, created_date)
                if type(result) == bool:
                    if result:
                        break
                else:
                    issue_date = result
                    break

            note['Дата дедлайн'] = issue_date

        notes[number_note] = note
        return True

# Создание списка для хранения данных об заметках
notes = []

break_all = False
update_notes = False
quantity_notes = len(notes)
while True:

    # Если количество заметок изменилось, то повторно выводим их
    if quantity_notes != len(notes) or update_notes:
        quantity_notes = len(notes)
        # Вывод данных об заметках на экран
        print_notes(notes)

    # Спросим о нужном действии
    while True:
        print()
        answer = input("""Введите номер нужного действия:
1 Добавить новую заметку
2 Обновить существующую заметку
3 Удалить заметки
4 Прекратить работу
> """)

        if answer.isdigit():
            if answer == '1':
                notes.append(create_note())
                break
            elif answer == '2':
                result = update_note()
                if result:
                    update_notes = True
                break
            elif answer == '3':
                result = del_notes()
                if result:
                    update_notes = True
                break
            elif answer == '4':
                break_all = True
                break
            else:
                print('Введено некорректное значение!')
        else:
            print('Введено некорректное значение!')

    # Прекращение цикла выбора действия
    if break_all:
        break
