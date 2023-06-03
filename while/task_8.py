my_number = None
my_list = []

while my_number != 0:
    my_number = int(input("Введите число: "))
    if my_number == 0:
        break
    my_list.append(my_number)


for i in range(0, len(my_list)):
    print(my_list[i])

print("Сумма равна:", sum(my_list))
