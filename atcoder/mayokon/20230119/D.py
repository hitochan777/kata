S = int(input())
MOD = 10**9+7

def make_array(*args):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]

N = S // 3
dp = make_array(N+1,S+1)
dp[0][0] = 1
acc = [0]
for s in range(S+1):
  acc.append((acc[-1]+dp[0][s])%MOD)

acc = acc[1:]
for n in range(N):
  for s in range(3, S+1):
    dp[n+1][s] = acc[s-3]

  acc = [0]
  for s in range(S+1):
    acc.append((acc[-1]+dp[n+1][s])%MOD)

  acc = acc[1:]
  
ans = 0
for i in range(1, N+1):
  ans += dp[i][S]
  ans %= MOD

print(ans)
