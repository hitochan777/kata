from atcoder.math import inv_mod
import math
MOD = 10**0 + 7

N = int(input())

def div_mod(a: int, b: int, mod: int) -> int:
  return (a * inv_mod(b, mod)) % mod

def n_choose_k(n, k, mod):
  if n < k:
    return 0

  p, q = 1, 1
  for i in range(k):
    p = (p * (n - i)) % mod
    q = (q * (i + 1)) % mod

  return (p * pow(q, mod-2, mod)) % mod

for k in range(1, N + 1):
  ans = 0
  for a in range(1, math.ceil(N / k) + 1):
    ans += n_choose_k(N - (k - 1) * (a - 1), a, MOD)
    ans %= MOD

  print(ans)
