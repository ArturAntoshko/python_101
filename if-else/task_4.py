age = int(input("Введите свой возраст: "))
if age in range(7, 18):
    print("40%")
elif age in range(18, 25):
    print("25%")
elif age >= 65:
    print("50%")