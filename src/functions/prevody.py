def mile(kilaky, onemile=0.621371):
    return kilaky*onemile

def kilaky(mile, onemile=0.621371):
    return mile/onemile

def celnaf(celsium, konstanta=((9/5)+32)):
    return celsium*konstanta

def fnacel(ef, konstanta=((9/5)+32)):
    return ef/konstanta

def cznaeu(czk, euro = 25):
    return czk/euro

def eunacz(eu, euro = 25):
    return eu*euro

if __name__ == "__main__":
    print(mile(2))
    print(kilaky(1.864113))
    print(celnaf(2))
    print(fnacel(101.4))
    print(cznaeu(50))
    print(eunacz(2))

