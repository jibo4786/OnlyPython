while True:
        cislo = input("Zadej celé číslo pro výpočet nebo slovo konec pro ukončení: ")
        if cislo.lower() == "konec":
            print("Konec programu")
            break

        try:
            vstup = int(cislo)
            print("Dvojnásobek:",vstup*2 )
        
        except ValueError:
             print("Chyba: musíš zadat číslo")