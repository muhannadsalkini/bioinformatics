import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_dosya = os.path.join(script_dir, "brca1.fasta")
output_dosya = os.path.join(script_dir, "brca1_minus_strand.fasta")

with open(input_dosya, "r") as f:
    satirlar = f.readlines()

dna_dizisi_parts = [satir.strip() for satir in satirlar if isinstance(satir, str) and not satir.startswith(">")]
dna_dizisi = "".join(dna_dizisi_parts)

harita = str.maketrans("ATCG", "TAGC")
tamamlayici = str(dna_dizisi).translate(harita)
ters_tamamlayici = "".join(reversed(tamamlayici))

with open(output_dosya, "w") as f_out:
    f_out.write(ters_tamamlayici)

print(f"İşlem tamamlandı. Dosya: {output_dosya}")
