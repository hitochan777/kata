from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

N = int(input())
deps = defaultdict(set)
for i in range(N):
  _, *P = list(int(x)-1 for x in input().split())
  deps[i] = set(P)

visited = set()
ans = []
def dfs(node):
  if node in visited:
    return

  visited.add(node)
  for nb in deps[node]:
    if nb in visited:
      continue

    dfs(nb)

  ans.append(str(node+1))

dfs(0)
print(" ".join(ans[:-1]))

