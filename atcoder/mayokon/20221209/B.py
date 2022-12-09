H, W = (int(x) for x in input().split())
rows = []
for _ in range(H):
  rows.append(input())

visited = set()
pos = (0,0)

dirs = {
  "U": (-1, 0),
  "D": (1, 0),
  "R": (0, 1),
  "L": (0,-1),
}
while True:
  x, y = pos
  if (x, y) in visited:
    print(-1)
    exit()

  visited.add(pos)
  dx, dy = dirs[rows[x][y]]
  if 0 <= x + dx < H and 0 <= y + dy < W:
    x += dx
    y += dy
  else:
    break

  pos = (x, y)

print(pos[0]+1, pos[1]+1)