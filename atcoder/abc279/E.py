from collections import defaultdict
N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
cnt = defaultdict(list)
for i, a in enumerate(A):
  cnt[a].append(i)

for i in range(M):
  p = 1 
  for a in 

