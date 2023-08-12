from collections import defaultdict

idx = defaultdict(list)
N, M = (int(x) for x in input().split())
S = list(input())
C = list(int(x) for x in input().split())
for i,c in enumerate(C):
  idx[c].append(i)

for c in range(1, M+1):
  cs = [S[i] for i in idx[c]]
  n = len(cs)
  for i in range(n):
    S[idx[c][i]] = cs[(i-1+n)%n]

print("".join(S))

