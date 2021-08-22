N = int(input())
S = input()
K = 10
MOD = 998244353

def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:]) for _ in range(args[0])]

dp = make_array(N+1, 1<<K, K)

for i in range(N):
  cur_c = ord(S[i]) - ord('A')
  for s in range(1<<K):
    for c in range(K):
      dp[i+1][s][c] = dp[i][s][c]
      if cur_c == c:
        dp[i+1][s][c] += dp[i][s][c]
        dp[i+1][s][c] %= MOD

  for s in range(1<<K):
    if (s >> cur_c) & 1 == 0:
      for c in range(K):
        dp[i+1][s | (1 << cur_c)][cur_c] += dp[i][s][c]
        dp[i+1][s | (1 << cur_c)][cur_c] %= MOD

  dp[i+1][1 << cur_c][cur_c] += 1
  dp[i+1][1 << cur_c][cur_c] %= MOD

# for i in range(N+1):
#   print(dp[i])

ans = 0
for s in range(1<<K):
  for c in range(K):
    ans += dp[N][s][c]
    ans %= MOD

print(ans)