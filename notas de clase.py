num = float(input("digite un numero: "))

if num < 0 or num > 10:
    print("incorrecto")

if num < 5:
    print("insuficiente")
elif num < 6:
    print("bien")

elif num < 7:
    print("Bien")

elif num < 9:
    print("Notable")
else:
    print("sobresaliente")



print(num)