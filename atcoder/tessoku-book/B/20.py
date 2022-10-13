N = int(input())
S = input()

dp = [[0] * (N+1) for _ in range(N)]
for i in range(N):
  dp[i][1] = 1

ans = 1
for l in range(2,N+1):
  for i in range(N-l+1):
    cands = []
    cands.append(dp[i+1][l-2])
    cands.append(dp[i+1][l-1])
    cands.append(dp[i][l-1])
    if S[i] == S[i+l-1]:
      cands.append(dp[i+1][l-2] + 2)

    dp[i][l] = max(cands)
    ans = max(ans, dp[i][l])

print(ans)

