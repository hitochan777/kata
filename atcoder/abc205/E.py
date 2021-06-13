import math

N, M, K = (int(x) for x in input().split())

ans = 0
MOD = 10**9 + 7

def n_choose_k(n, k, mod):
  p, q = 1, 1
  for i in range(k):
    p = (p * (n - i)) % mod
    q = (q * (i + 1)) % mod

  return (p * pow(q, mod-2, mod)) % mod

for i in range(N+M):
  if (i + K) % 2 != 0:
    continue

  w = (i + K) // 2
  b = i - w
  if w < 0 or b < 0 or w > N - 1 or b > M:
    continue

  c = n_choose_k(w + b, w, MOD)
  ans += c % MOD

ans = (n_choose_k(N+M, N, MOD) - ans) % MOD
print(ans)
 