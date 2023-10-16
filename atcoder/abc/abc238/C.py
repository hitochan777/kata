N = int(input())
l = len(str(N))

if l == 1:
  print(N * (N+1) // 2)
  exit()

MOD = 998244353
ans = 9 * 10 // 2
for i in range(1,l-1):
  n = (10**i) * 9
  ans += n * (n+1) // 2
  ans %= MOD

n = N - 10**(l-1) + 1
ans += n * (n+1) // 2
ans %= MOD

print(ans)