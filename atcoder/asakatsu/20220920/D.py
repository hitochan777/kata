import math


N, K = (int(x) for x in input().split())

if K == 0:
  print(N**2)
  exit()

ans = 0
for b in range(K+1, N+1):
  diff = N // b * max(b-K, 0) + max(N % b - (K-1), 0)
  ans += diff 

print(ans)
