H, W = (int(x) for x in input().split())
g = []
for _ in range(H):
  g.append(input())

def dfs(i, j, visited):
  if (i, j) in visited:
    return (0, 0)

  visited.add((i,j))
  c1, c2 = 0, 0
  if g[i][j] == ".":
    c1 = 1
  else:
    c2 = 1

  for dx, dy in [(0, 1), (1, 0)]:
    if i + dx >= H or j + dy >= W:
      continue

    if g[i+dx][j+dy] == g[i][j]:
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
