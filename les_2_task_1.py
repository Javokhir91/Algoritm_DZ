operation = input('Введите знак операции [+ - * /] или 0 для завершения: ')

while operation != '0':

    if operation == '+':
        a, b = map(float, input('Введите через пробел 2 числа: ').split())
        result = a + b
    elif operation == '-':
        a, b = map(float, input('Введите через пробел 2 числа: ').split())
        result = a - b
    elif operation == '*':
        a, b = map(float, input('Введите через пробел 2 числа: ').split())
        result = a * b
    elif operation == '/':
        a, b = map(float, input('Введите через пробел 2 числа: ').split())
        if b != 0:
            result = a / b
        else:
            print('Деление на 0 не возможно!')
            operation = input('Введите знак операции [+ - * /] или 0 для завершения: ')
            continue
    else:
        print('Ошибка в знаке операции!')
        operation = input('Введите знак операции [+ - * /] или 0 для завершения: ')
        continue

    print(f'{a} {operation} {b} = {result}')
    operation = input('Введите знак операции [+ - * /] или 0 для завершения: ')

print('До скорой встречи!')
