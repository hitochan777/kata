N, W = (int(x) for x in input().split())
items = []
value_sum = 0
for _ in range(N):
  w, v = (int(x) for x in input().split())
  items.append((w,v))
  value_sum += v

dp = [[10**18] * (value_sum+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
  for v in range(value_sum+1):
    dp[i+1][v] = dp[i][v]
    new_v = v - items[i][1]
    if new_v >= 0:
      dp[i+1][v] = min(dp[i+1][v], dp[i][new_v]+items[i][0])

ans = max(v for v, w in enumerate(dp[N]) if w <= W)
print(ans)