N = int(input())
S = input()
MOD = 998244353
dp = [ [0] * 11 for _ in range(N+1)]

# for c in range(10):
#   dp[0][c] = 1
dp[0][0] = 1

for i in range(N):
  total = sum(dp[i]) % MOD
  for c in range(11):
    dp[i+1][c] = dp[i][c]
    if c == 0:
      continue

    if S[i] == chr(ord('A') + c - 1):
      dp[i+1][c] += total
      dp[i+1][c] %= MOD

    dp[i+1][c] %= MOD

print(dp)
print(sum(dp[N]))