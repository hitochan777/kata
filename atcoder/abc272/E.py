from collections import defaultdict
from math import ceil


N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

vals = defaultdict(set)
for i in range(N):
  if A[i] >= N:
    continue

  l = 0 if A[i] >= 0 else ceil(-A[i] // (i+1))-1
  for j in range(l, M):
    val = A[i] + (j+1) * (i+1)
    if val > N:
      break

    vals[j].add(val)

for m in range(M):
  for i in range(N+1):
    if i not in vals[m]:
      print(i)
      break