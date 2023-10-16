from collections import defaultdict
import heapq
import sys

sys.setrecursionlimit(10**6)

N = int(input())
g = defaultdict(list)
degs = defaultdict(int)

for _ in range(N):
  u, v = (int(x)-1 for x in input().split())
  g[u].append(v)
  g[v].append(u)
  degs[u] += 1
  degs[v] += 1

h = []

for node in range(N):
  heapq.heappush(h, (degs[node], node))

visited = set()
while len(h) > 0:
  deg, node = heapq.heappop(h)
  if deg >= 2:
    break

  if node in visited:
    continue

  visited.add(node)
  for nb in g[node]:
    if nb in visited:
      continue

    degs[nb] -= 1
    heapq.heappush(h, (degs[nb], nb))

loop = set()
for node in range(N):
  if node not in visited:
    loop.add(node)

def dfs(node, visited, root_dict, root):
  if node in visited:
    return

  root_dict[node] = root
  visited.add(node)
  for nb in g[node]:
    if nb in visited or nb in loop:
      continue

    dfs(nb, visited, root_dict, root)

root_dict = {}
for node in loop:
  visited = set()
  dfs(node, visited, root_dict, node)

Q = int(input())
for _ in range(Q):
  x, y = (int(x)-1 for x in input().split())
  if root_dict[x] == root_dict[y]:
    print("Yes")
  else:
    print("No")