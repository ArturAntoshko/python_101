bukva_A = int(input("введите первую букву: "))
bukva_B = int(input("введите вторую букву: "))
bukva_C = int(input("введите третью букву: "))

if bukva_A + bukva_B > bukva_C:
    print("можно")
elif bukva_A + bukva_C > bukva_B:
    print("можно")
elif bukva_B + bukva_C > bukva_A:
    print("можно")
else:
    print("нельзя")
