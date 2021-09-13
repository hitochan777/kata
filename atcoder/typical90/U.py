from collections import defaultdict
import sys

readline = sys.stdin.buffer.readline
read = sys.stdin.buffer.read

sys.setrecursionlimit(1000000)

N, M = (int(x) for x in readline().split())
G = defaultdict(list) 
RG = defaultdict(list)
for _ in range(M):
  A, B = (int(x) for x in readline().split())
  G[A-1].append(B-1)
  RG[B-1].append(A-1)

post_orders = []
def dfs(node, visited, g):
  if node in visited:
    return
  
  visited.add(node)
  for nb in g[node]:
    if nb not in visited:
      dfs(nb, visited, g)

  post_orders.append(node)

def dfs2(node, visited, g):
  if node in visited:
    return 0
  
  cnt = 1
  visited.add(node)
  for nb in g[node]:
    if nb not in visited:
      cnt += dfs2(nb, visited, g)

  return cnt

visited = set()
for node in range(N):
  dfs(node, visited, G)

total = 0
# print(nodes)
visited = set()
for node in post_orders[::-1]:
  cnt = dfs2(node, visited, RG)
  # print(node, cnt)
  total += cnt * (cnt-1) // 2

print(total)