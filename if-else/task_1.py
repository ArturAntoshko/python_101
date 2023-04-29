age = int(input("введите возраст: "))

if age >= 18 and age < 85:
    print("вы можете водить машину!")
elif age < 18 and age >= 0:
    a = 18 - age
    print(f"вернитесь через {a} лет")
else:
    print("вы не можете водить машину")