dosya_yolu = "rosalind_dna.txt"

with open(dosya_yolu, "r") as f:
    dna = f.read().strip()

a = dna.count('A')
c = dna.count('C')
g = dna.count('G')
t = dna.count('T')

print(a, c, g, t)
