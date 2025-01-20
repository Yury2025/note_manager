created_date = '20-01-2025'
issue_date = '30-01-2025'

# Вариант для формата 'ДД-ММ-ГГГГ'
print('Дата создания заметки: ', created_date[0:5])
print('Дата истечения заметки (дедлайн): ', issue_date[0:5])

# Вариант для формата 'ДД ММММ ГГГГ'
created_date = '20 января 2025'
issue_date = '30 января 2025'

temp_created_date = created_date[::-1]
temp_created_date = temp_created_date[5:]
print('Дата создания заметки: ', temp_created_date[::-1])
temp_issue_date = issue_date[::-1]
temp_issue_date = temp_issue_date[5:]
print('Дата истечения заметки (дедлайн): ', temp_issue_date[::-1])
