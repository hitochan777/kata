import sys
from collections import defaultdict


N, M, K = (int(x) for x in sys.stdin.readline().split())
A = list(int(x)-1 for x in sys.stdin.readline().split())
graph = defaultdict(list)
for i in range(N-1):
  U, V = (int(x) for x in sys.stdin.readline().split())
  U, V = U-1, V-1
  graph[U].append((V,i))
  graph[V].append((U,i))

count = defaultdict(int)
def dfs(node, prev, goal):
  if node == goal:
    return True

  for nb, edge_num in graph[node]:
    if nb == prev:
      continue

    if dfs(nb, node, goal):
      count[edge_num] += 1
      return True

  return False

def make_array(*args, default=int):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]


def solve():
  MOD = 998244353
  for i in range(M-1):
    dfs(A[i], -1, A[i+1])

  C = [count[i] for i in range(N-1)]
  S = sum(C)
  if (S + K) % 2 != 0 or S + K < 0:
    return 0

  dp = make_array(N, S + K + 1)
  dp[0][0] = 1
  for i in range(N-1):
    for j in range(S + K + 1):
      dp[i+1][j] += dp[i][j]
      if j >= C[i]:
        dp[i+1][j] += dp[i][j-C[i]]

      dp[i+1][j] %= MOD

  return dp[N-1][(S + K) // 2]

print(solve())