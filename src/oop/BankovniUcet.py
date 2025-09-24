class BankovniUcet:
    def __init__(self, majitel: str, zustatek: float = 0.0):
        self.majitel = majitel
        self.zustatek = float(zustatek)

    def vloz(self, castka: float) -> None:
        if castka <= 0:
            print("Neplatná částka. Musíš vložit více než 0 Kč.")
            return
        self.zustatek += castka
        print(f"Na účet bylo vloženo {castka: .2f} Kč. Nový zůstatek jee {self.zustatek: .2f} Kč.")
    
    def vyber(self, castka: float) -> None:
        if castka <= 0:
            print("Nemůžeš vybrat 0 Kč")
        elif castka > self.zustatek:
            print("Nemůžeš vybrat větší částku než je aktuální zůstatek!")
            return
        self.zustatek -= castka
        print(f"Z účtu bylo vybráno {castka: .2f} Kč. Nový zůstatek jee {self.zustatek: .2f} Kč.")
    
    def zobraz(self)->None:
        print(f"Na účtu zákazníka {self.majitel} je aktuální zůstatek {self.zustatek: .2f} Kč.")

    def __repr__(self)->str:
        return f"<Na účtu zákazníka {self.majitel} je aktuální zůstatek {self.zustatek: .2f} Kč.>"
    
if __name__ == "__main__":
    u = BankovniUcet("Jiří", 500)

while True:
    print("Aplikace bankoního účtu.")
    print(f"Majitel účtu: {u.majitel} ___________________ Aktuální zůstatek: {u.zustatek}")
    print("Volba možností:")
    print("1 - Vložit peníze")
    print("2 - Vybrat peníze")
    print("3 - Zobrazit aktuální stav účtu")
    print("4 - Odhlásit se z bankovnictví")


    volba = int(input("Vyber co chceš udělat: "))
    

        
    try:
            if volba == 1:
                castka = int(input("Jakou částku v Kč chceš vložit: "))
                v = u.vloz(castka)
                print(v)
                
            elif volba == 2:
                castka = int(input("Jakou částku v Kč chceš vybrat: "))
                vy = u.vyber(castka)
                print(vy)
            elif volba == 3:
                z = u.zobraz()
                print(z)
            elif volba == 4:
                print("Byl jste odhlášen z bankovnictví!")
                break
            else:
                print("Neplatná volba!")
    except ValueError:
            print("Chyba: musíš zadat číslo")





     