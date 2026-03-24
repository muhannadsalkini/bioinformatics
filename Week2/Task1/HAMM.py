import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_dir, "rosalind_hamm.txt")

with open(input_file, "r") as f:
    satirlar = f.readlines()
    s1 = satirlar[0].strip()
    s2 = satirlar[1].strip()

mutasyon_sayisi = sum(1 for i in range(len(s1)) if s1[i] != s2[i])

print(mutasyon_sayisi)
