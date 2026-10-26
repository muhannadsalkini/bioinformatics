# Bioinformatics Exercises

Python solutions to introductory bioinformatics problems from [Rosalind](https://rosalind.info), organized by week, plus a FASTA reverse-complement exercise. Each script reads its input dataset from the same folder and prints or writes the answer.

## 🧬 Problems Solved

| Week | Script | Problem | What it does |
| --- | --- | --- | --- |
| 1 | `INI1.py` | [INI1](https://rosalind.info/problems/ini1/) | Installing Python (prints the Zen of Python) |
| 1 | `INI2.py` | [INI2](https://rosalind.info/problems/ini2/) | Variables and arithmetic (sum of squares) |
| 1 | `INI3.py` | [INI3](https://rosalind.info/problems/ini3/) | String slicing |
| 1 | `INI4.py` | [INI4](https://rosalind.info/problems/ini4/) | Sum of odd integers in a range |
| 1 | `INI5.py` | [INI5](https://rosalind.info/problems/ini5/) | Print every even-numbered line of a file |
| 1 | `INI6.py` | [INI6](https://rosalind.info/problems/ini6/) | Word frequency count with a dictionary |
| 2 | `Task1/DNA.py` | [DNA](https://rosalind.info/problems/dna/) | Count A, C, G, T nucleotides |
| 2 | `Task1/RNA.py` | [RNA](https://rosalind.info/problems/rna/) | Transcribe DNA into RNA |
| 2 | `Task1/REVC.py` | [REVC](https://rosalind.info/problems/revc/) | Reverse complement of a DNA strand |
| 2 | `Task1/HAMM.py` | [HAMM](https://rosalind.info/problems/hamm/) | Hamming distance (point mutations) between two strands |
| 2 | `Task2/BRCA1.py` | — | Reverse complement of a gene sequence read from a FASTA file |
| 3 | `PROT.py` | [PROT](https://rosalind.info/problems/prot/) | Translate an mRNA string into a protein using the codon table |
| 3 | `SUBS.py` | [SUBS](https://rosalind.info/problems/subs/) | Find all (overlapping) positions of a motif in DNA |
| 3 | `MPRT.py` | [MPRT](https://rosalind.info/problems/mprt/) | Fetch protein sequences from UniProt and locate the N-glycosylation motif `N{P}[ST]{P}` with a lookahead regex |

## 🛠 Tech Stack

- Python 3 (standard library: `os`, `re`)
- [`requests`](https://pypi.org/project/requests/) — only for `MPRT.py`, which downloads sequences from UniProt

## 🚀 Running

```bash
git clone https://github.com/muhannadsalkini/bioinformatics.git
cd bioinformatics
pip install requests        # only needed for Week3/MPRT.py

python Week2/Task1/DNA.py
python Week3/MPRT.py        # needs internet access
```

Scripts resolve their input file relative to their own location, so they can be run from any directory.

- Week 1 and Week 2 `Task1` scripts print the answer to the console.
- `Task2/BRCA1.py` writes the reverse-complement sequence to `brca1_minus_strand.fasta`.
- Week 3 scripts write their answers to `rosalind_*_output.txt` (MPRT also prints them).

To solve a new Rosalind dataset, replace the matching `rosalind_*.txt` file and rerun the script.

## 📁 Project Structure

```
Week1/              # Python Village warm-ups (INI1–INI6) + input datasets
Week2/
├── Task1/          # DNA, RNA, REVC, HAMM + input datasets
└── Task2/          # FASTA reverse complement (input + generated output)
Week3/              # PROT, SUBS, MPRT + inputs and generated outputs
```

> Note: despite its name, `Week2/Task2/brca1.fasta` contains a VEGFA gene record (*Oryctolagus cuniculus*, NC_091436.1); the script works on any single-record FASTA file.

Variable names and console messages are partly in Turkish.

## 📄 License

[MIT](LICENSE)
