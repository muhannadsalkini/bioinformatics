dosya_yolu = "rosalind_rna.txt"

with open(dosya_yolu, "r") as f:
    dna = f.read().strip()

rna = dna.replace('T', 'U')

print(rna)
