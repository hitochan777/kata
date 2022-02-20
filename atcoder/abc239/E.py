import sys
from collections import defaultdict
import heapq

sys.setrecursionlimit(10**6)

def dfs(node, parent):
  nums = [X[node]]
  for nb in g[node]:
    if nb == parent:
      continue

    dfs(nb, node)
    nums += largest[nb]

  nums.sort(reverse=True)
  largest[node] = nums[:20]


g = defaultdict(list)
largest = defaultdict(list)
N, Q = (int(x) for x in input().split())
X = list(int(x) for x in input().split())
for _ in range(N-1):
  A, B = (int(x) for x in input().split())
  A, B = A-1, B-1
  g[A].append(B)
  g[B].append(A)

dfs(0, -1)

for _ in range(Q):
  V, K = (int(x) for x in input().split())
  V, K = V-1, K-1
  print(largest[V][K])