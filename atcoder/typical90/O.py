from atcoder.math import inv_mod
import math
MOD = 10**9 + 7

N = int(input())

def div_mod(a: int, b: int, mod: int) -> int:
  return (a * inv_mod(b, mod)) % mod

def pow_mod(a: int, n: int, mod: int) -> int:
  res = 1
  while n > 0:
    if n & 1:
      res = (res * a) % mod
    
    a = (a * a) % mod
    n >>= 1
  
  return res

class CombinationCalculator:
  def __init__(self, n: int, mod: int):
    self.mod = mod
    self.cache = [None] * (n + 1)

  def _init_cache(self, n: int) -> None:
    res = 1
    for i in range(1, self.n + 1):
      res *= i
      res %= self.mod

  def factorial(self, n: int) -> int:
    return self.cache[n]

  def n_choose_k(self, n: int, k: int) -> int:
    if n < k:
      return 0

    p = self.factorial(n)
    q = self.factorial(k)
    r = self.factorial(n-k)
    return (p * pow_mod() *pow_mod(q, mod-2, mod)) % mod

for k in range(1, N + 1):
  ans = 0
  for a in range(1, math.ceil(N / k) + 1):
    res = n_choose_k(N - (k - 1) * (a - 1), a, MOD)
    # print(N - (k - 1) * (a - 1), a, MOD, res)
    ans += res
    ans %= MOD

  print(ans)
