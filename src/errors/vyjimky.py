while True:
    try:
        cislo = int(input("Zadej číslo (nebo 0 pro konce): "))
        if cislo == 0:
            print("Konec programu: ")
            break
        print("Odmocnina: ", cislo**0.5)

    except ValueError as e:
        print("Chyba: musíš zadat celé číslo!", e)

    finally:
        print("---iterace ukončena---")