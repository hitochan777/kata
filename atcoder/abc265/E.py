MOD = 998244353
N, M = (int(x) for x in input().split())
A, B, C, D, E, F = (int(x) for x in input().split())
obstacles = set()
for _ in range(M):
  X, Y = (int(x) for x in input().split())
  obstacles.add((X,Y)) 

def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, N+1, N+1)
for n in range(N):
  for x in range(1,N):
    for y in range(1,N):
      new_x = A * x + y * C + (n - x - y) * E
      new_y = B * x + y * D + (n - x - y) * F
      if (new_x, new_y) not in obstacles:
        dp[n+1][x][y] += dp[n][x][y]
        
      new_x = A * x + y * C + (n - x - y) * E
      new_y = B * x + y * D + (n - x - y) * F
      if (new_x, new_y) not in obstacles:
        dp[n+1][x][y] += dp[n][x-1][y]     

      new_x = A * x + y * C + (n - x - y) * E
      new_y = B * x + y * D + (n - x - y) * F
      if (new_x, new_y) not in obstacles:
        dp[n+1][x][y] += dp[n][x-1][y-1]

      dp[n+1][x][y] %= MOD

total = 0
for x in range(N+1):
  for y in range(N+1):
    total += dp[N][x][y]

print(total)