dosya_yolu = "rosalind_ini6.txt"

with open(dosya_yolu, "r") as f:
    kelimeler = f.read().split()

sozluk = {}

for kelime in kelimeler:
    if kelime in sozluk:
        sozluk[kelime] += 1
    else:
        sozluk[kelime] = 1

for anahtar, deger in sozluk.items():
    print(anahtar, deger)
