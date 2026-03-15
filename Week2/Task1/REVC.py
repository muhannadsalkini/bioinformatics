dosya_yolu = "rosalind_revc.txt"

with open(dosya_yolu, "r") as f:
    dna = f.read().strip()

harita = str.maketrans("ATCG", "TAGC")
tamamlayici = dna.translate(harita)
ters_tamamlayici = tamamlayici[::-1]

print(ters_tamamlayici)
