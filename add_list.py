username = input('Введите имя пользователя: ')
title1 = input('Введите 1 заголовок заметки: ')
title2 = input('Введите 2 заголовок заметки: ')
title3 = input('Введите 3 заголовок заметки: ')

list_title = [title1, title2, title3]

content = input('Введите описание заметки: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания заметки в формате "ДД-ММ-ГГГГ": ')
issue_date = input('Введите дату истечения заметки (дедлайн) в формате "ДД-ММ-ГГГГ": ')

print('Имя пользователя: ', username)
print('Варианты заголовков заметки: ', '\"'+list_title[0]+'\"'+', '+'\"'+list_title[1]+'\"'+', '+'\"'+list_title[2]+'\"')
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания заметки: ', created_date)
print('Дата истечения заметки (дедлайн): ', issue_date)