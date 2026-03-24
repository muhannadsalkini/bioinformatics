import os

script_dir = os.path.dirname(os.path.abspath(__file__))
dosya_yolu = os.path.join(script_dir, "rosalind_rna.txt")

with open(dosya_yolu, "r") as f:
    dna = f.read().strip()

rna = dna.replace('T', 'U')

print(rna)
