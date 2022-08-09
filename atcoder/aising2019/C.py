import sys

sys.setrecursionlimit(10**6)

H, W = (int(x) for x in input().split())
g = []
for _ in range(H):
  g.append(input())

def dfs(i, j, visited):
  visited.add((i,j))
  c1, c2 = 0, 0
  if g[i][j] == ".":
    c1 = 1
  else:
    c2 = 1

  for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
    if i + dx >= H or j + dy >= W or i + dx < 0 or j + dy < 0:
      continue

    if g[i+dx][j+dy] == g[i][j]:
      continue

    if (i + dx, j + dy) in visited:
      continue

    c = dfs(i + dx, j + dy, visited)
    c1 += c[0]
    c2 += c[1]

  return (c1, c2)

ans = 0
visited = set()
for i in range(H):
  for j in range(W):
    c1, c2 = dfs(i, j, visited)
    ans += c1 * c2

print(ans)
