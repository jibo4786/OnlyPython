from pathlib import Path

seznam = Path("todo.txt")

while True:

    print(" === TODO appka ===")
    print("-MENU-")
    print("1 - Přidat úkol")    
    print("2 - Seznam úkolů")
    print("3 - Ukončit")

    volba = input("Co chceš udělat: ").strip()

    if volba == "1":
        ukol = input("Zadej úkol: ").strip()
        if not ukol:
            print("Prázdný úkol neuložím.")
            continue
        with open(seznam, "a", encoding="UTF-8") as f:
            f.write(ukol+"\n")
        print("Uloženo.")
        
    elif volba == "2":
        try:
            with open(seznam, "r", encoding="UTF-8") as f:
                print("== SEZNAM ÚKOLŮ ==\n")
                for i, radek in enumerate(f, start=1):
                    print(f"{i}.{radek.rstrip()}")
            
        except FileNotFoundError as e:
            print("Chyba: soubor pro čtení nebyl nalezen: {e} ")
    
    elif volba == "3":
        print("KONEC")
        break
    else:
        print("Neplatná volba")