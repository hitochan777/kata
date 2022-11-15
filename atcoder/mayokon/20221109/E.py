N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
D = 42

dp = [[-10**18] * 2 for _ in range(D+1)]
dp[0][0] = 0
for d in range(D):
  for l in range(2):
    if dp[d][l] == -10**18:
      continue

    shift = D-d-1
    mask = 1 << shift
    zero, one = 0, 0
    for a in A:
      if a & mask == 0:
        zero += 1
      else:
        one += 1
    if l == 0:
      if K & mask == 0:
        dp[d+1][0] = max(dp[d+1][0], dp[d][l] + one * mask)
      else:
        dp[d+1][0] = max(dp[d+1][0], dp[d][l] + one * mask)
        dp[d+1][1] = max(dp[d+1][1], dp[d][l] + zero * mask)
    else:
        dp[d+1][1] = max(dp[d+1][1], dp[d][l] + max(one, zero) * mask)

print(max(dp[D][0], dp[D][1]))
    

    

  