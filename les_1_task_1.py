
number = int(input("Введите трехзначное целое число : "))

a = number // 100
b = number // 10 % 10
c = number % 10

d = a + b + c
g = a * b * c


print(f'сумма {d} , произведение {g}')
