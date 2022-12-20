D, G = (int(x) for x in input().split())
G /= 100
num = 0
P = []
C = []
for _ in range(D):
  p, c = (int(x) for x in input().split())
  c //= 100
  P.append(p)
  C.append(c)
  num += p

dp = [[-10**18]*(num+1) for _ in range(D+1)]
dp[0][0] = 0
for d in range(D):
  for n in range(num+1):
    for k in range(P[d]):
      dp[d+1][min(num, n+k)] = max(dp[d+1][min(num, n+k)], dp[d][n]+k*(d+1))
    
    dp[d+1][min(num, n+P[d])] = max(dp[d+1][min(num, n+k)], dp[d][n]+k*P[d]+C[d])

ans = None
for i, score in enumerate(dp[D]):
  if score >= G:
    ans = i
    break

print(ans)
