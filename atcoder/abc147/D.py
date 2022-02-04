N = int(input())
A = list(int(x) for x in input().split())
MOD = 10**9 + 7

ans = 0
for i in range(60):
  mask = 1 << i
  zero, one = 0, 0
  for a in A:
    if a & mask == 0:
      zero += 1
    else:
      one += 1

  ans += zero * one * mask
  ans %= MOD

print(ans)