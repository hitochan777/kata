import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

g = defaultdict(list)
N = int(input())
for _ in range(N-1):
  a, b = (int(x) for x in input().split())
  a, b = a-1, b-1
  g[a].append(b)
  g[b].append(a)

ranges = [None] * N
def dfs(node, parent, num):
  max_val = num
  second = False
  for nb in g[node]:
    if nb == parent:
      continue

    if second:
      max_val += 1

    max_val = dfs(nb, node, max_val)
    second = True

  ranges[node] = (num, max_val)
  return max_val

dfs(0, -1, 1)
for l, r in ranges:
  print(l, r)
