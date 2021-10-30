from collections import defaultdict
N = int(input())
MOD = 46
AS, BS, CS = defaultdict(int), defaultdict(int), defaultdict(int)
A = list(int(x) % MOD for x in input().split())
B = list(int(x) % MOD for x in input().split())
C = list(int(x) % MOD for x in input().split())
for a in A:
  AS[a] += 1

for b in B:
  BS[b] += 1

for c in C:
  CS[c] += 1

total = sum(ac * bc * cc for a, ac in AS.items() for b, bc in BS.items() for c, cc in CS.items() if (a + b + c) % MOD == 0)
print(total)
