# http://rosalind.info/problems/subs/
# Finding a Motif in DNA

with open('./rosalind_ini1.txt') as f:
    data = f.readlines()
    main1 = data[1].strip()
    sub1 = data[0].strip()
    for i in range(len(main1)):
        if main1[i:i+len(sub1)] == sub1:
            print(str(i), end=" ")
    print("")