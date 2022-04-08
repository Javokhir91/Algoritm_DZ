
year = int(input("year : "))

if year % 4 != 0:
    print("Не високосный год!")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосный год!")
    else:
        print("Не високосный год!")
else:
    print("Високосный год!")
