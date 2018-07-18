# http://rosalind.info/problems/gc/
# Computing GC Content

from Bio import SeqIO
max_val = 0
max_id = ''
with open('./rosalind_ini1.txt') as f:
    for i in (SeqIO.parse(f , 'fasta')):
        gc_content = (str(i.seq).count("G") + str(i.seq).count("C"))/ len(str(i.seq))
        if(gc_content > max_val):
            max_val = gc_content
            max_id = i.id
print(max_id)
print("%2.8g" % (max_val*100))