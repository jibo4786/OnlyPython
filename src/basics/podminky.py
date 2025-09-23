vek = int(input("Zadej svůj věk: "))

if vek < 0:
    print("To nedává smysl.")
elif vek < 18:
    print("Jsi mladší než 18 let.")
elif vek < 65:
    print("Jsi dospělý.")
else:
    print("Jsi senior.")

x = 5
print(x > 0 and x < 10)
print(x < 0 and x > 10)
print(not (x == 5))
