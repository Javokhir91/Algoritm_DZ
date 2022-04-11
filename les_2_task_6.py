import random

b = random.randint(1, 100)
a = None
count = 0
max_count = 10
while b != a:
    count += 1
    if count > max_count:
        print('Вы проиграли!')
        break
    print(f'Попытка № {count}')
    a = int(input('Введите число : '))
    if b < a:
        print('Ваше число больше загаданного')
    elif b > a:
        print('Ваше число меньше загаданного')
else:
    print('ПОБЕДА!!!')
