from pathlib import Path
from datetime import datetime

soubor = Path("log.txt")

zprava = input("Zadej zprávu pro denní log: ")

cas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
zaznam=f"[{cas}]{zprava}\n"

with open(soubor, "a", encoding="utf-8")as f:
    f.write(zaznam)

print("\n=== OBSAH LOGU ===")
with open(soubor, "r", encoding="utf-8") as f:
    print(f.read())