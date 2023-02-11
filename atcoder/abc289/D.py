N = int(input())
A = list(int(x) for x in input().split())
M = int(input())
banned = set(int(x) for x in input().split())
X = int(input())

dp = [False] * (X+1)
dp[0] = True

for i in range(1, X+1):
  dp[i] = any(i-a >= 0 and dp[i-a] and ((i-a) not in banned) for a in A)

if dp[X]:
    print("Yes")
else:
    print("No")
