from atcoder.math import inv_mod
import math
MOD = 10**9 + 7

N = int(input())

def div_mod(a: int, b: int, mod: int) -> int:
  return (a * inv_mod(b, mod)) % mod

class CombinationCalculator:
  def __init__(self, n: int, mod: int):
    self.mod = mod
    self.cache = [None] * (n + 1)
    self.cache_inv = [None] * (n + 1)
    self._init_cache(n)

  def _init_cache(self, n: int) -> None:
    res = 1
    self.cache[0] = 1
    self.cache_inv[0] = 1
    for i in range(1, n + 1):
      res *= i
      res %= self.mod
      self.cache[i] = res
      self.cache_inv[i] = pow(res, self.mod - 2, self.mod)

  def factorial(self, n: int) -> int:
    return self.cache[n]

  def factorial_inv(self, n: int) -> int:
    return self.cache_inv[n]

  def n_choose_k(self, n: int, k: int) -> int:
    if n < k:
      return 0

    return (self.factorial(n) * self.factorial_inv(k) * self.factorial_inv(n-k)) % self.mod

cc = CombinationCalculator(N, MOD)
for k in range(1, N + 1):
  ans = 0
  for a in range(1, math.ceil(N / k) + 1):
    res = cc.n_choose_k(N - (k - 1) * (a - 1), a)
    # print(N - (k - 1) * (a - 1), a, MOD, res)
    ans += res
    ans %= MOD

  print(ans)