# http://rosalind.info/problems/dna/
# Counting DNA Nucleotides

with open('./rosalind_ini1.txt') as f:
    data = f.read().strip()
    print(data.count("A"), data.count("C"), data.count("G"), data.count("T"))
