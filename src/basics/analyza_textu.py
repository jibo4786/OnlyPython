veta = "Jelenovy pivo nelej!"
bez_mezer = veta.replace(" ", "")
slova = veta.split()
nejdelsi = max(slova, key=len)

frekvence = {}
for slovo in slova:
    slovo = slovo.lower().strip(".,!?")
    frekvence[slovo] = frekvence.get(slovo, 0)+1

print(frekvence)

print(len(bez_mezer))
print(len(slova))
print(nejdelsi)




