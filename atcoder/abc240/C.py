N, X = (int(x) for x in input().split())
ab = []
for _ in range(N):
  ab.append(list(int(x) for x in input().split()))

def make_array(*args):
  if len(args) == 0:
    return False

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1,X+1)
dp[0][0] = True

for i in range(0,N):
  for j in range(1,X+1):
    if j >= ab[i][0]:
      dp[i+1][j] = dp[i+1][j] or dp[i][j-ab[i][0]]
      
    if j >= ab[i][1]:
      dp[i+1][j] = dp[i+1][j] or dp[i][j-ab[i][1]]

if dp[N][X]:
  print("Yes")
else:
  print("No")