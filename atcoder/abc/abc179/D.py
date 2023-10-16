N, K = map(int, input().split())
intervals = []
for _ in range(K):
    l, r = map(int, input().split())
    intervals.append((l, r))

dp = [0] * (N + 1)
sdp = [0] * (N + 1)
dp[1] = 1
sdp[1] = 1
for i in range(2, N + 1):
    for l, r in intervals:
        dp[i] +=  (sdp[max(0, i-l)] - sdp[max(0, i-r-1)]) % 998244353

    sdp[i] += (dp[i] + sdp[i-1]) % 998244353

print(dp[N] % 998244353)