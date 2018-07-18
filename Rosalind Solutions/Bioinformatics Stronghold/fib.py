# http://rosalind.info/problems/fib/
# Rabbits and Recurrence Relations

def rec(n,k):
    if n==1 : return 1
    elif n==2: return k
    n1 = rec(n-1, k)
    n2 = rec(n-2, k)
    if(n <= 4):
        return(n1 + n2)
    return n1 + n2*k

with open('./rosalind_ini1.txt') as f:
    data = f.read().strip()
    n,k = list(map(int,data.split()))
    # n: number of months
    # k: number of offsprings reproduced each time
    print(rec(n,k))
