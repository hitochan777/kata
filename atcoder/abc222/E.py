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
def dfs(start, goal):
  stack = [(start, -1)]
  parents = {start: (-1, -1)}

  while len(stack) > 0:
    node, prev = stack.pop()
    if node == goal:
      break

    for nb, edge_num in graph[node]:
      if nb == prev:
        continue

      stack.append((nb, node))
      parents[nb] = (node, edge_num)

  p = goal
  while True:
    node, edge_num = parents[p]
    if node == -1:
      break

    count[edge_num] += 1
    p = node

def make_array(*args, default=int):
  if len(args) == 0:
    return 0

  return [make_array(*args[1:]) for _ in range(args[0])]


def solve():
  MOD = 998244353
  for i in range(M-1):
    dfs(A[i], A[i+1])

  C = [count[i] for i in range(N-1)]
  S = sum(C)
  if (S + K) % 2 != 0 or S + K < 0:
    return 0

  P = (S + K) // 2
  dp = make_array(P+1)
  dp[0] = 1
  for i in range(N-1):
    for j in range(P, C[i]-1, -1):
      if j >= C[i]:
        dp[j] += dp[j-C[i]]
        dp[j] %= MOD

  return dp[P]

print(solve())