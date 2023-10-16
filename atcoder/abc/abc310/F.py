N = int(input())
A = list(int(x) for x in input().split())
target = 10  # 目標の和

mod = 998244353  # modの値

dp = [[0] * (target + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(target + 1):
        for k in range(1, min(j, A[i-1]) + 1):
            dp[i][j] += dp[i-1][j-k]
            dp[i][j] %= mod
        dp[i][j] += dp[i-1][j]
        dp[i][j] %= mod

result = dp[N][target]
print(result)