import os

script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "rosalind_subs.txt")
output_path = os.path.join(script_dir, "rosalind_subs_output.txt")


with open(input_path, "r") as f:
   lines = f.readlines()
   s = lines[0].strip()
   t = lines[1].strip()


results = []
len_t = len(t)
for i in range(len(s) - len_t + 1):
   if s.startswith(t, i):
       results.append(str(i + 1))


with open(output_path, "w") as out:
   out.write(" ".join(results))