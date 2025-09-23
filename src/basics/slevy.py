vek = int(input("Zadej svůj věk prosím: "))

if vek < 18:
    print("Dětská sleva")
elif vek > 65:
    print("Seniorská sleva")
elif (vek >= 18 and vek <= 27):
    isic = input("Jsi vlastník ISIC? Zadej ano nebo ne.").strip().lower()

    if isic == "ano":
        print("Studentská sleva!")
    elif isic == "ne":
        print("bez slevy khámo!")

else:
    print("bez slevy khámo!")
