from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

N = int(input())
graph = defaultdict(set)
for _ in range(N-1):
  u, v = (int(x) for x in sys.stdin.readline().split())
  u, v = u-1, v-1
  graph[u].add(v)
  graph[v].add(u)

count = [1] * N
ans = [0] * N
def root_dfs(node = 0, parent = None):
  for child in graph[node]:
    if child == parent:
      continue

    root_dfs(child, node)
    count[node] += count[child]
    ans[node] += ans[child] + count[child]

def child_dfs(node = 0, parent = None):
  for child in graph[node]:
    if child == parent:
      continue

    ans[child] = ans[node] - count[child] + N - count[child]
    child_dfs(child, node)

root_dfs()
child_dfs()

for val in ans:
  print(val)