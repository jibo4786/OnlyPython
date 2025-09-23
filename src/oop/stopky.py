import time

class Stopky:
    def __init__(self):
        self.start = None
        self.end = None
    
    def spust(self):
        self.start = time.time()
        self.end = None
        print("Stopky spuštěny!")

    def zastav(self):
        if self.start is None:
            print("Nejdřív musíš spustit stopky!")
            return
        self.end = time.time()
        print("Stopky zastaveny!")
    
    def cas(self):
        if self.start is None:
            return 0
        if self.end is None:
            return time.time() - self.start
        return self.end - self.start
    
    def __repr__(self):
        return f"<Stopky: {self.cas():.2f} s>"
    
if __name__ == "__main__":
    s = Stopky()

    while True:

     print("1 - spustit")
     print("2 - zastavit")
     print("3 - ukončit")
     print("4 - časovač")
     vyber = int(input("Zvol volbu: "))

     if vyber == 1:
         s.spust()
    
    
     elif vyber == 2:
           s.zastav()
           print(s)
    
     elif vyber == 3:
        print("Konec")
        break
    
     elif vyber == 4:
         casovac = int(input("Na kolik sekud chceš časovat: "))
         s.spust()
         time.sleep(casovac)
         print(f"Časovač se zastavil za {casovac} sekund/y!" )
     else:
        print("Špatná volba bitch!")