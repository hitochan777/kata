from math import gcd, ceil, sqrt
from functools import reduce

N = int(input())
Ai = list(int(x) for x in input().split())
def sieve(max_n): 
    spf = [0] * max_n
    spf[1] = 1
    for i in range(2, max_n):
        spf[i] = i 
        
    for i in range(4, max_n, 2): 
        spf[i] = 2

    for i in range(3, ceil(sqrt(max_n))): 
        if (spf[i] == i): 
            for j in range(i * i, max_n, i): 
                if (spf[j] == j): 
                    spf[j] = i 

    return spf

def factorize(x, spf): 
	ret = list() 
	while (x != 1): 
		ret.append(spf[x]) 
		x = x // spf[x] 

	return ret 

def is_pairwise_coprime(Ai):
    spf = sieve(max(Ai) + 1)
    primes = set()
    for a in Ai:
        factors = factorize(a, spf)
        for factor in set(factors):
            if factor in primes:
                return False

            primes.add(factor)

    return True

if is_pairwise_coprime(Ai) :
    print("pairwise coprime")
elif reduce(gcd, Ai, Ai[0]) == 1:
    print("setwise coprime")
else:
    print("not coprime")