from collections import defaultdict, deque
N, M, K = (int(x) for x in input().split())

edges = []
for i in range(M):
  A, B, C = (int(x) for x in input().split())
  edges.append((A-1, B-1, C))

E = list(int(x)-1 for x in input().split())
dp = [10**18] * N
dp[0] = 0

for e in E:
  a, b, c = edges[e]
  dp[b] = min(dp[b], dp[a] + c)

if dp[N-1] == 10**18:
  print(-1)
else:
  print(dp[N-1])