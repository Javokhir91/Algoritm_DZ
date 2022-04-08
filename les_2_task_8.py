number_find = int(input('Введите, какую цифру мы ищем: '))
n = int(input('Введите количество чисел для поиска: '))
result = 0

for i in range(n):
    number = input('Введите натуральное число: ')

    for num in number:
        if int(num) == number_find:
            result += 1

print(f'Количество вхождений во всех числах: {result}')