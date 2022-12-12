import math
N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
F = list(int(x) for x in input().split())
A.sort()
F.sort(reverse=True)
ng, ok = -1, 10**18
while ok - ng > 1:
  m = (ok+ng) >> 1
  total = 0
  for a, f in zip(A,F):
    k = max(math.ceil(a - m/f), 0)
    total += k

  if total <= K:
    ok = m
  else:
    ng = m

print(ok)