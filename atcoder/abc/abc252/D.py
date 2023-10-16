from collections import Counter

N = int(input())
A = list(int(x) for x in input().split())
maxA = max(A)
cnt = Counter(A)
def make_array(*args, default=int):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(maxA+1, 4)
dp[0][0] = 1
for i in range(maxA):
  dp[i+1][0] = dp[i][0]
  for j in range(1,4):
    dp[i+1][j] = dp[i][j] + dp[i][j-1] * cnt[i+1]

print(dp[maxA][3])