import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

N = int(input())
g = defaultdict(list)
for i in range(N-1):
  a, b = (int(x) for x in input().split())
  a, b = a-1, b-1
  g[a].append((b, i))
  g[b].append((a, i))

colors = [0] * (N-1)
color_set = set()

def dfs(node, parent=-1, parent_color=0):
  offset = 0
  used = set([parent_color])
  color = 1
  for i, (nb, e) in enumerate(g[node], start=1):
    if nb == parent:
      continue

    while color in used:
      color += 1

    colors[e] = color 
    color_set.add(color)
    used.add(color)
    dfs(nb, node, color)

dfs(0)
print(len(color_set))
for color in colors:
  print(color)
