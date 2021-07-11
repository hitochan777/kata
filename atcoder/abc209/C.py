ans = 1
MOD = 10**9 + 7
N = int(input())
C = list(int(x) for x in input().split())
C.sort()
for i, c in enumerate(C):
  ans = (ans * max(0, c-i)) % MOD

print(ans)