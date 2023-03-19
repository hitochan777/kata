from math import gcd

T = int(input())
for _ in range(T):
  N, D, K = (int(x) for x in input().split())
  K -= 1
  g = gcd(N, D)
  Ng = N // g
  Dg = D // g 
  ans = ((K * Dg) % Ng) * g + (K // Ng)
  print(ans)
  