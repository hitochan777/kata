from collections import defaultdict 
from itertools import permutations

N = int(input())
A = []
for _ in range(N):
  a = list(int(x) for x in input().split())
  A.append(a)

M = int(input())
m = defaultdict(set)

for _ in range(M):
  X, Y = (int(x) for x in input().split())
  X, Y = X-1, Y-1
  m[X].add(Y)
  m[Y].add(X)

min_val = 100000
people = list(range(N))
for permutation in permutations(people, N):
  ok = False
  for i in range(N-1):
    a, b = permutation[i], permutation[i+1]
    if a in m[b] or b in m[a]:
      break
  else:
    ok = True
  
  if ok:
    total = sum(A[j][i] for i, j in enumerate(permutation))
    min_val = min(min_val, total)

print(min_val if min_val < 100000 else -1)