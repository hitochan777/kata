from bisect import bisect_left
N = int(input())
boxes = []
for _ in range(N):
  X, Y = (int(x) for x in input().split())
  boxes.append((X,Y))

boxes.sort()
A = [y for _, y in boxes]

dp = [0] * (N+1)
L = [10**18] * (N+1)
L[0] = 0
for i in range(N):
  dp[i+1] = bisect_left(L, A[i])
  L[dp[i+1]] = A[i]

print(max(dp))

