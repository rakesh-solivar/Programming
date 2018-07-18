# http://rosalind.info/problems/iprb/
# Mendel's First Law

with open('./rosalind_ini1.txt') as f:
    data = f.read().strip()
    data = list(map(int,data.split()))
    k = data[0]
    m = data[1]
    n = data[2]
    total = k + m + n
    total_1 = total - 1
    kk = (k / total) * ((k-1) / total_1)
    km = ((k/total) * (m/total_1)) + ((m/total) * (k/total_1))
    kn = ((k/total) * (n/total_1)) + ((n/total) * (k/total_1))
    mm = (m/total) * ((m-1)/total_1)
    mn = ((m/total) * (n/total_1)) + ((n/total) * (m/total_1))
    nn = (n/total) * ((n-1)/total_1)

    certain = kk + km + kn
    mm_res = 0.75 * mm
    mn_res = 0.5 * mn
    print("%2.5g" % float(certain + mm_res + mn_res))

