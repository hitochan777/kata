from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

N = int(input())
C = list(int(x) for x in input().split())
g = defaultdict(list)
for _ in range(N-1):
  A, B = (int(x)-1 for x in input().split())
  g[A].append(B)
  g[B].append(A)

good = []
cnt = defaultdict(int)
def dfs(node, parent=-1):
  global cnt
  global good
  cnt[C[node]] += 1
  if cnt[C[node]] == 1:
    good.append(node)

  for nb in g[node]:
    if nb == parent:
      continue

    dfs(nb, node)

  cnt[C[node]] -= 1

dfs(0, )

good.sort()
for i in good:
  print(i+1)