N, S = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
dp = [[False]*(S+1) for _ in range(N+1)]
for i in range(N+1):
  dp[i][0] = True

for i in range(N):
  for s in range(1,S+1):
    dp[i+1][s] |= dp[i][s]
    if s >= A[i]:
      dp[i+1][s] |= dp[i][s-A[i]]

if not dp[N][S]:
  print(-1)
  exit()

s = S
ans = []
for i in range(N-1,-1,-1):
  if s >= A[i] and dp[i][s-A[i]]:
    ans.append(i+1)
    s -= A[i]

print(len(ans))
print(*ans[::-1])


