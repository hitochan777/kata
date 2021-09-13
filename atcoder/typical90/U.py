from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

N, M = (int(x) for x in input().split())
G = defaultdict(list) 
RG = defaultdict(list)
for _ in range(M):
  A, B = (int(x) for x in input().split())
  G[A-1].append(B-1)
  RG[B-1].append(A-1)

def create_dfs(g, acc, initialize):
  visited = set()
  def dfs(node):
    if node in visited:
      return initialize(None)
    
    cur = initialize(node)
    visited.add(node)
    for nb in g[node]:
      cur = acc(cur, dfs(nb))

    return cur 

  return dfs

visit = create_dfs(G, lambda cur, res: cur + res, lambda node: [node] if node is not None else [])
count = create_dfs(RG, lambda cur, res: cur + res, lambda node: 1 if node is not None else 0)

nodes = []
for node in range(N):
  nodes = visit(node) + nodes

total = 0
# print(nodes)
for node in nodes:
  cnt = count(node)
  if cnt == 0:
    continue
  # print(node, cnt)
  total += cnt * (cnt-1) // 2

print(total)