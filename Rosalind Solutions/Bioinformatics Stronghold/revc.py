# http://rosalind.info/problems/revc/
# Complementing a Strand of DNA

with open('./rosalind_ini1.txt') as f:
    data = f.read().strip()
    data = "".join(reversed(data))
    stri = ""
    for i,j in enumerate(data):
        if(j=="A"):
            stri += ("T")
        if(j=="T"):
            stri += ("A")
        if(j=="C"):
            stri += ("G")
        if(j=="G"):
            stri += ("C")
    print(stri)