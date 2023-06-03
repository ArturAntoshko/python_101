import random


random_number = random.randint(1, 100)
user_number = 0

while user_number != random_number:
    user_number = int(input("Введите число: "))

print("вы выграли целое ничего!!!")
