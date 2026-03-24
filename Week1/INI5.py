import os

script_dir = os.path.dirname(os.path.abspath(__file__))
dosya_yolu = os.path.join(script_dir, "rosalind_ini5.txt")

with open(dosya_yolu, "r") as f:
    satirlar = f.readlines()

sayac = 1
for satir in satirlar:
    if sayac % 2 == 0:
        print(satir.strip())
    sayac += 1
