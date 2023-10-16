from collections import Counter
N = int(input())
S = input()

MOD = 10**9 + 7
cnts = Counter(S)
ans = 1
for cnt in cnts.values():
  ans *= cnt + 1
  ans %= MOD

ans += MOD - 1
ans %= MOD
print(ans)