year = int(input("введите год: "))

if year % 4 == 0 and year % 100 != 0:
    print("год является високосным")
elif year % 4 == 0 and year % 100 == 0:
    print("год не является високосным")
else:
    print("год не является високосным")
