import math

N, M, K = (int(x) for x in input().split())

ans = 0
MOD = 10**9 + 7

def n_choose_k(n, k, mod):
  if n < k:
    return 0

  p, q = 1, 1
  for i in range(k):
    p = (p * (n - i)) % mod
    q = (q * (i + 1)) % mod

  return (p * pow(q, mod-2, mod)) % mod

if N - M > K:
  print(0) 
else:
  print((n_choose_k(N+M, N, MOD) - n_choose_k(N+M, M+K+1, MOD))%MOD)