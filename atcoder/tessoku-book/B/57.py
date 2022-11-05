N, K = (int(x) for x in input().split())
dp = [[0] * (N+1) for _ in range(31)]

def get_sum(n):
  s = 0
  while n > 0:
    s += n % 10
    n //= 10

  return s

for i in range(N+1):
  dp[0][i] = i - get_sum(i)

for i in range(1, 31):
  for j in range(N+1):
    dp[i][j] = dp[i-1][dp[i-1][j]]

for i in range(1,N+1):
  cur = i
  for j in range(31):
    if (K >> j) & 1 == 1:
      cur = dp[j][cur]

  print(cur)