from collections import defaultdict
from atcoder.dsu import DSU

N, M, K = (int(x) for x in input().split())
dsu = DSU(N)
non_candidates = defaultdict(set)
for _ in range(M):
  a, b = (int(x)-1 for x in input().split()) 
  dsu.merge(a,b)
  non_candidates[a].add(b)
  non_candidates[b].add(a)

for _ in range(K):
  a, b = (int(x)-1 for x in input().split()) 
  if not dsu.same(a,b):
    continue

  non_candidates[a].add(b)
  non_candidates[b].add(a)
  
ans = []
for i in range(N):
  ans.append(dsu.size(i) - len(non_candidates[i])-1)
  
print(*ans)
    