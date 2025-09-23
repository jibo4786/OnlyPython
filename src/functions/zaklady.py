def soucet(a, b):
    return a + b

def pozdrav(jmeno="neznámý"):
    return f"Ahoj, {jmeno}!"

def mocnina(cislo, exponent=2):
    return cislo**exponent

if __name__ == "__main__":
    print(soucet(3,5))
    print(pozdrav("Jiří"))
    print(pozdrav())
    print(mocnina(4))
    print(mocnina(2, 3))