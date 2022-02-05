from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

N = int(input())
C = list(int(x) for x in input().split())
g = defaultdict(list)
for _ in range(N-1):
  A, B = (int(x) for x in input().split())
  A, B = A-1, B-1
  g[A].append(B)
  g[B].append(A)

visited = set()
ans = defaultdict(bool)
used = defaultdict(bool)
def dfs(node):
  if node in visited:
    return

  visited.add(node)
  if not used[C[node]]:
    ans[node] = True

  used[C[node]] = True
  for nb in g[node]:
    dfs(nb)

  if ans[node]:
    used[C[node]] = False

dfs(0)

for i in range(N):
  if ans[i]:
    print(i+1)