from collections import Counter
from functools import lru_cache

@lru_cache(10**6)
def get_perm(n, mod):
  ans = 1
  for i in range(2, n+1):
    ans *= i
    ans %= mod

  return ans

N = int(input())
T = []
for _ in range(N):
  t = int(input())
  T.append(t)

T.sort()
cnt = Counter(T)
vals = [0]
for t in T:
  vals.append(vals[-1] + t)

MOD = 10**9 + 7
num_ways = 1
for v in cnt.values():
  num_ways *= get_perm(v, MOD)
  num_ways %= MOD

print(sum(vals))
print(num_ways)