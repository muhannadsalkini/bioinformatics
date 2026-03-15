dosya_yolu = "rosalind_hamm.txt"

with open(dosya_yolu, "r") as f:
    satirlar = f.readlines()
    s1 = satirlar[0].strip()
    s2 = satirlar[1].strip()

mutasyon_sayisi = 0

for i in range(len(s1)):
    if s1[i] != s2[i]:
        mutasyon_sayisi += 1

print(mutasyon_sayisi)
