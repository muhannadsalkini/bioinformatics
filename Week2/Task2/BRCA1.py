input_dosya = "brca1.fasta"
output_dosya = "brca1_minus_strand.fasta"

with open(input_dosya, "r") as f:
    satirlar = f.readlines()

dna_dizisi = ""
for satir in satirlar:
    if not satir.startswith(">"):
        dna_dizisi += satir.strip()

harita = str.maketrans("ATCG", "TAGC")
tamamlayici = dna_dizisi.translate(harita)
ters_tamamlayici = tamamlayici[::-1]

with open(output_dosya, "w") as f_out:
    f_out.write(ters_tamamlayici)

print(f"İşlem tamamlandı. Dosya: {output_dosya}")
