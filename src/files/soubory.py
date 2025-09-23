from pathlib import Path

soubor = Path("data.txt")

with open(soubor, "w", encoding="utf-8") as f:
    f.write("První řádek\n")
    f.write("Druhý řádek\n")

with open(soubor, "a", encoding="utf-8") as f:
    f.write("Třetí řádek\n")

with open(soubor, "r", encoding="utf-8") as f:
    obsah = f.read()

print("Obsah souboru:")
print(obsah)