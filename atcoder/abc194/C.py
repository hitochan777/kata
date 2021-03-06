from collections import Counter
N = list(int(x) for x in input().split())[0]
A = list(int(x) for x in input().split())
cnts = Counter(A)

total = 0
for i in range(-200, 201):
    for j in range(i+1, 201):
        total += ((cnts[i] * cnts[j]) * ((i - j)** 2))

print(total)

