N, W = (int(x) for x in input().split())
items = []
for _ in range(N):
  w, v = (int(x) for x in input().split())
  items.append((w,v))

dp = [[0] * (W + 1) for _ in range(N+1)]
for i in range(N):
  for w in range(W+1):
    dp[i+1][w] = dp[i][w]
    new_w = w - items[i][0]
    if new_w >= 0:
      dp[i+1][w] = max(dp[i+1][w], dp[i][new_w]+items[i][1]) 

print(max(dp[N]))