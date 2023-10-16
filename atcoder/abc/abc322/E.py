N, K, P = (int(x) for x in input().split())

INF = 10**18
def make_array(*args):
  if len(args) == 0:
    return INF

  return [make_array(*args[1:]) for _ in range(args[0])]

C = []
A = []

dp = make_array(N+1, P+1, P+1, P+1, P+1, P+1)
dp[0][0][0][0][0][0] = 0
for _ in range(N):
  c, *a = (int(x) for x in input().split())
  C.append(c)
  while len(a) < 5:
    a.append(0)

  A.append(a)

for i in range(N):
  for k1 in range(0, P+1):
    for k2 in range(0, P+1):
      for k3 in range(0, P+1):
        for k4 in range(0, P+1):
          for k5 in range(0, P+1):
            dp[i+1][k1][k2][k3][k4][k5] = min(dp[i+1][k1][k2][k3][k4][k5], dp[i][k1][k2][k3][k4][k5])
            dp[i+1][min(k1+A[i][0], P)][min(k2+A[i][1], P)][min(k3+A[i][2], P)][min(k4+A[i][3], P)][min(k5+A[i][4], P)] = min(
              dp[i+1][min(k1+A[i][0], P)][min(k2+A[i][1], P)][min(k3+A[i][2], P)][min(k4+A[i][3], P)][min(k5+A[i][4], P)],
              dp[i][k1][k2][k3][k4][k5] + C[i]
            )

ans = INF
if K == 1:
  ans = dp[N][P][0][0][0][0]
if K == 2:
  ans = dp[N][P][P][0][0][0]
if K == 3:
  ans = dp[N][P][P][P][0][0]
if K == 4:
  ans = dp[N][P][P][P][P][0]
if K == 5:
  ans = dp[N][P][P][P][P][P]

if ans == INF:
  print(-1)
else:
  print(ans)