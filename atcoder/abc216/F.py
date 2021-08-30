def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:]) for _ in range(args[0])]

N = int(input())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
C = list(zip(A, B))
C.sort()
Bmax = 5001
dp = make_array(N+1, Bmax) 
dp[0][0] = 1

for i in range(1, N+1):
  for j in range(Bmax):
    # dp[i+1][j] = total[j-C[i][1]]
    if j >= C[i-1][1]:
      dp[i][j] = sum(dp[k][j-C[i-1][1]] for k in range(i))

ans = 0
for i in range(N):
  for j in range(C[i][0]+1):
    ans += dp[i+1][j]

print(ans)
