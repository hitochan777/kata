MOD = 10**9 + 7

n, a, b = (int(x) for x in input().split())

def n_choose_k(n, k, mod):
  p, q = 1, 1
  for i in range(k):
    p = (p * (n - i)) % mod
    q = (q * (i + 1)) % mod

  return (p * pow(q, mod-2, mod)) % mod

ans = (pow(2, n, MOD) - n_choose_k(n, a, MOD) - n_choose_k(n, b, MOD) - 1) % MOD
print(ans)
