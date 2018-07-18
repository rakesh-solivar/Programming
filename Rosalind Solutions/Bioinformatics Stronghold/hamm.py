# http://rosalind.info/problems/hamm/
# Counting Point Mutations

with open('./rosalind_ini1.txt') as f:
    data = f.read().split("\n")
    count = 0
    for i in range(len(data[0])):
        if not (data[0][i] == data[1][i]):
            count+=1
    print(count)
