historie = []

while True:
    print("\n=== Kalkulačka ===")
    print("1) Součet")
    print("2) Rozdíl")
    print("3) Násobek")
    print("4) Podíl")
    print("5) Zobrazit historii")
    print("6) Konec")

    volba = input("Vyber operaci (1-6): ")

    if volba == "6":
        print("Konec programu!")
        break

    if volba == "5":
        print("=== HISTORIE ===")
        for zaznam in historie:
            print(zaznam)
        continue

    try:
        a = float(input("Zadej první číslo: "))
        b = float(input("Zadej druhé číslo: "))
    except ValueError:
        print("Chyba: musíš zadat číslo!")
        continue

    if volba == "1":
        vysledek = a + b
        zapis = f"{a} + {b} = {vysledek}"
    elif volba == "2":
        vysledek = a - b
        zapis = f"{a} - {b} = {vysledek}"
    elif volba == "3":
        vysledek = a * b
        zapis = f"{a} * {b} = {vysledek}"
    elif volba == "4":
        if b == "0":
            print("Chyba: dělení nulou není dovoleno!!!")
            continue
        vysledek = a / b
        zapis = f"{a} / {b} = {vysledek}"
    else:
        print("Neplatná volba!")
        continue

    print("výsledek: ",vysledek)
    historie.append(zapis)