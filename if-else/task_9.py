age = int(input("вес пингвина: "))
if age <= 30 and age >= 15:
    print("дайте пингвину 5 рыб")
elif age >= 5 and age <= 15:
    print("дайте пингвину 2.5 рыб")
elif age >= 30 and age <= 50:
    print("дайте пингвину 10 рыб")
else:
    print("Введите настоящий вес пингвина")