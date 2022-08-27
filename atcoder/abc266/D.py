from collections import defaultdict


N = int(input())
def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

T = 0
A = defaultdict(int)
for i in range(N):
  t, x, a = (int(x) for x in input().split())
  T = max(T, t)
  A[(t, x)] = a

dp = make_array(T+1, 5)
for t in range(T):
  for x in range(5):
    if x - 1 >= 0:
      dp[t+1][x] = max(dp[t+1][x], dp[t][x-1])

    dp[t+1][x] = max(dp[t+1][x], dp[t][x])
    if x + 1 < 5:
      dp[t+1][x] = max(dp[t+1][x], dp[t][x+1])

    if t + 1 >= x:
      dp[t+1][x] += A[(t+1,x)]

# print(dp, T)
print(max(dp[T]))