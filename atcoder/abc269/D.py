import sys

sys.setrecursionlimit(10000)
N = int(input())
s = set()
for _ in range(N):
  X, Y = (int(x) for x in input().split())
  s.add((X,Y))

dirs = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
def dfs(node, visited):
  if node in visited:
    return

  visited.add(node)
  for dx, dy in dirs:
    new_node = (node[0] + dx, node[1] + dy)
    if new_node in s and new_node not in visited:
      dfs(new_node, visited)

visited = set()
cnt = 0
for node in s:
  if node not in visited:
    cnt += 1
    dfs(node, visited)

print(cnt)