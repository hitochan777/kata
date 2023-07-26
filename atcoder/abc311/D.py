N, M = (int(x) for x in input().split())
g = []
for _ in range(N):
  S = input()
  g.append(S)

q = [(1,1,0,0)]
visited = set()
visited2 = set()
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
  x, y, dx, dy = q.pop()
  visited.add((x, y))
  visited2.add((x, y, dx, dy))
  if dx == 0 and dy == 0:
    for dx2, dy2 in dirs:
      nx, ny = x + dx2, y + dy2
      if g[nx][ny] == "." and (nx, ny, dx2, dy2) not in visited2:
        q.append((nx, ny, dx2, dy2))
  else:
    nx, ny = x + dx, y + dy
    if g[nx][ny] == "." and (nx, ny, dx, dy) not in visited2:
      q.append((nx, ny, dx, dy))
    elif g[nx][ny] == "#":
      q.append((x, y, 0, 0))

print(len(visited))