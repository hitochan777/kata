N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
C = list(zip(A, B))

def make_array(*args):
  if len(args) == 0:
    return False

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N, 2)
dp[0][0] = True
dp[0][1] = True
for i in range(0, N-1):
  for j in range(2):
    dp[i+1][j] = (dp[i][0] and (abs(C[i+1][j] - C[i][0]) <= K)) or (dp[i][1] and (abs(C[i+1][j] - C[i][1]) <= K))

if dp[N-1][0] or dp[N-1][1]:
  print("Yes")
else:
  print("No")