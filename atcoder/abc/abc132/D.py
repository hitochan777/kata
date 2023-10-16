N, K = (int(x) for x in input().split())
MOD = 10**9 +7

def h(n, k):
  return n_choose_k(n+k-1, k-1, MOD)

def n_choose_k(n, k, mod):
  p, q = 1, 1
  for i in range(k):
    p = (p * (n - i)) % mod
    q = (q * (i + 1)) % mod

  return (p * pow(q, mod-2, mod)) % mod


for i in range(1, K+1):
  ans = h(K-i, i) * h(N-K-(i-1), i+1)
  ans %= MOD
  print(ans)