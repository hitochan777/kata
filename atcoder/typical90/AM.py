import sys
from collections import defaultdict
sys.setrecursionlimit(10**5+1)
N = int(input())
g = defaultdict(list)
for _ in range(N-1):
  a, b = (int(x) for x in input().split())
  a, b = a-1, b-1
  g[a].append(b)
  g[b].append(a)

contributions = defaultdict(int)
def dfs(node, pre=-1):
  contributions[node] = 1
  for nb in g[node]:
    if nb == pre:
      continue

    dfs(nb, node)
    contributions[node] += contributions[nb]

dfs(0)
total = sum((N - val) * val for val in contributions.values())
print(total)