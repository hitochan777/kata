N = int(input())
T = list(int(x) for x in input().split()) 

S = sum(T)
dp = [[False] * (S // 2 + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = True

for i in range(1, N+1):
    for j in range(1, S // 2 + 1):
        dp[i][j] = dp[i-1][j]
        if j >= T[i-1]:
            dp[i][j] = dp[i][j] or dp[i-1][j-T[i-1]]


m = max(s for s, ok in enumerate(dp[N]) if ok)
print(S - m)