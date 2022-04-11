a = input('Введите натуральное число: ')
chetnoe = 0
nechetnoe = 0
for numeric in a:
    if int(numeric) % 2 == 0:
        chetnoe += 1
    else:
        nechetnoe += 1

print(f'Вданном числе четных цифр: {chetnoe} , не четных цифр: {nechetnoe}')
