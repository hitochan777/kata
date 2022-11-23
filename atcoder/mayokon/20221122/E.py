N, K = (int(x) for x in input().split())

MOD = 998244353
dp = [0] * N
dp[0] = 1
acc = [0, 1]
ranges = []
for _ in range(K):
  L, R = (int(x) for x in input().split())
  ranges.append((L,R))

for i in range(1,N):
  for l, r in ranges:
    dp[i] += acc[max(0, i-l+1)] - acc[max(0, i-r)]
    dp[i] %= MOD

  acc.append(acc[-1]+dp[i])

# print(dp)
print(dp[N-1])
