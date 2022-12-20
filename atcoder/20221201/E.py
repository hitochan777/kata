import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
N = int(input())
g = defaultdict(list)
for _ in range(N-1):
  a, b = (int(x)-1 for x in input().split())
  g[a].append(b)
  g[b].append(a)

def dfs(parents={}, leaves=[], node=0, parent=-1):
  parents[node] = parent
  children = 0
  for nb in g[node]:
    if nb == parent:
      continue

    children += 1
    dfs(parents, leaves, nb, node)

  if children == 0:
    leaves.append(node)

parents = {}
leaves = []
dfs(parents, leaves)

gg

print(parents, leaves)