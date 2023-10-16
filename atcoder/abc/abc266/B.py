N = int(input())
MOD = 998244353
N %= MOD
for x in range(998244353):
  if x % MOD == N:
    print(x)
    exit()
