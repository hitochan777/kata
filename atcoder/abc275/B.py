A, B, C, D, E, F = (int(x) for x in input().split())
MOD = 998244353

ans = (A * B * C - D * E * F) % MOD
print(ans)