
print("Введите три разных чисел")

a = int(input("Введите первое число : "))
b = int(input("Введите вторую число : "))
c = int(input("Введите третую число : "))

if b < a < c or c < a < b:
    print(f'средняя {a}')
elif a < b < c or c < b < a:
    print(f'средняя {b}')
else:
    print(f'средняя {c}')
