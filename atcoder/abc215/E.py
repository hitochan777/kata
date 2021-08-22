N = int(input())
S = input()
MOD = 998244353

def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, 1<<10, 10)

for i in range(N):
  cur_c = ord(S[i]) - ord('A')
  for s in range(1<<10):
    for c in range(10):
      dp[i+1][s][c] = dp[i][s][c]
      if cur_c == c:
        dp[i+1][s][c] += dp[i][s][c]
        dp[i+1][s][c] %= MOD

  for s in range(1<<10):
    if (s >> cur_c) & 1 == 0:
      for c in range(10):
        dp[i+1][s | (1 << cur_c)][c] += dp[i][s][c]
        dp[i+1][s | (1 << cur_c)][c] %= MOD

  dp[i+1][1 << cur_c][cur_c] += 1
  dp[i+1][1 << cur_c][cur_c] %= MOD

ans = 0
for s in range(1<<10):
  for c in range(10):
    ans += dp[N][s][c]
    ans %= MOD

print(ans)