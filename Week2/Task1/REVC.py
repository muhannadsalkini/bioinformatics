import os

script_dir = os.path.dirname(os.path.abspath(__file__))
dosya_yolu = os.path.join(script_dir, "rosalind_revc.txt")

with open(dosya_yolu, "r") as f:
    dna = f.read().strip()

harita = str.maketrans("ATCG", "TAGC")
tamamlayici = dna.translate(harita)
ters_tamamlayici = "".join(reversed(tamamlayici))

print(ters_tamamlayici)
