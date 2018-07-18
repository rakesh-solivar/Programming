# http://rosalind.info/problems/rna/
# Transcribing DNA into RNA

with open('./rosalind_ini1.txt') as f:
    data = f.read().strip()
    print(data.replace("T", "U"))
