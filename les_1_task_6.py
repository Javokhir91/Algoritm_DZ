# Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.


num = int(input('Введите порядковый номер буквы: '))
num += ord('a') - 1
a = chr(num)
print(f'Ваша буква: {a}')
