import sys
sys.setrecursionlimit(10**8)
N, M = (int(x) for x in input().split())

MOD = 998244353
cnt = 0
def f(n):
  if n == 2:
    return (M * (M-1)) % MOD

  return (M * pow(M-1, n-1, MOD) - f(n-1) + MOD) % MOD

print(f(N))