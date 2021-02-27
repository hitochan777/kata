from collections import Counter 
from math import comb

K = int(input())
S = input()
T = input()
counts = [K] * 10

for n, c in Counter(S[:4]).items():
    counts[int(n)] -= c
    counts[int(n)] = max(counts[int(n)], 0)

for n, c in Counter(T[:4]).items():
    counts[int(n)] -= c
    counts[int(n)] = max(counts[int(n)], 0)

def calc_score(s):
    cnts = [0] * 10
    for c in s:
        cnts[int(c)] += 1
    
    return sum(int(n) * 10 ** c for n, c in enumerate(cnts))

def calc_combs(a, b):
    if a == b:
        return comb(counts[a], 2) * 2

    # print(counts)
    return counts[a] * counts[b] 

# print(counts)
total_combs = 0
for a in range(1, 10):
    for b in range(1, 10):
        a_score = calc_score(S[:4] + str(a))
        b_score = calc_score(T[:4] + str(b))
        if a_score <= b_score:
            continue

        # print((a,b))

        combs = calc_combs(a, b)
        total_combs += combs

print(total_combs / (comb(9 * K - 8, 2) * 2))