import math

N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

ok, ng = 10**9+1, 0
while ok - ng > 1:
  l = (ok + ng) >> 1
  total = 0
  for a in A:
    if a > l:
      total += math.ceil(a / l) - 1
    
  if total <= K:
    ok = l
  else:
    ng = l
    
print(ok)