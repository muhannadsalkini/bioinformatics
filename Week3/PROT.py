import os

script_dir = os.path.dirname(os.path.abspath(__file__))

codon_table = {
   "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
   "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
   "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
   "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
   "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
   "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
   "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
   "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
   "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
   "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
   "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
   "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
   "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
   "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
   "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
   "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}


input_path = os.path.join(script_dir, "rosalind_prot.txt")
output_path = os.path.join(script_dir, "rosalind_prot_output.txt")


with open(input_path, "r") as file:
   rna_sequence = file.read().strip()


protein_parts = []

for i in range(0, len(rna_sequence) - 2, 3):
   codon = rna_sequence[i] + rna_sequence[i+1] + rna_sequence[i+2]
   amino_acid = codon_table.get(codon)
  
   if amino_acid == "Stop":
       break
   elif amino_acid:
       protein_parts.append(amino_acid)

protein = "".join(protein_parts)


with open(output_path, "w") as out_file:
   out_file.write(protein)