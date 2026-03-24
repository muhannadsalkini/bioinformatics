import requests
import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))


input_file = os.path.join(script_dir, "rosalind_mprt.txt")
output_file = os.path.join(script_dir, "rosalind_mprt_output.txt")


with open(input_file, "r") as f:
   uniprot_ids = [line.strip() for line in f if line.strip()]


motif_regex = r'(?=(N[^P][ST][^P]))'


with open(output_file, "w") as out:
   for raw_id in uniprot_ids:
       clean_id = raw_id.split('_')[0]
       url = f"https://www.uniprot.org/uniprot/{clean_id}.fasta"
      
       response = requests.get(url)
      
       if response.status_code == 200:
           satirlar = response.text.strip().split('\n')
           protein_dizisi = "".join(satirlar[1:])
          
           pozisyonlar = []
           for eslesme in re.finditer(motif_regex, protein_dizisi):
               pozisyonlar.append(str(eslesme.start() + 1))
          
           if pozisyonlar:
               print(raw_id)
               print(" ".join(pozisyonlar))
               out.write(raw_id + "\n")
               out.write(" ".join(pozisyonlar) + "\n")
