from functools import lru_cache 
from atcoder.math import inv_mod
MOD = 998244353

@lru_cache(10**6)
def fn(n: int):
  if n > N:
    return 0

  if n == N:
    return 1

  total = sum(fn(k * n) for k in range(2, 7)) % MOD
  return (total * inv_mod(5, MOD)) % MOD

N = int(input())
print(fn(1))