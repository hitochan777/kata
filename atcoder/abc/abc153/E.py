H, N = (int(x) for x in input().split())
A = []
B = []
for _ in range(N):
  a, b = (int(x) for x in input().split())
  A.append(a)
  B.append(b)

def make_array(*args):
  if len(args) == 0:
    return 10**18

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, H+1)
for i in range(N+1):
  dp[i][H] = 0

for i in range(N):
  for h in range(H,-1,-1):
    dp[i+1][h] = min(dp[i+1][h], dp[i][h])
    dp[i+1][max(0,h-A[i])] = min(dp[i+1][max(0,h-A[i])], dp[i+1][h] + B[i])

print(dp[N][0])


