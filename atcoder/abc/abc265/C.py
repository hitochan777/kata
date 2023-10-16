H, W = (int(x) for x in input().split())
g = []
for _ in range(H):
  g.append(input())

visited = set()
x, y = 0, 0
while True:
  if (x, y) in visited:
    print(-1)
    exit()

  visited.add((x,y))
  if g[x][y] == "U":
    if x != 0:
      x -= 1
    else:
      break
  elif g[x][y] == "D":
    if x != H-1:
      x += 1
    else:
      break
  elif g[x][y] == "L":
    if y != 0:
      y -= 1
    else:
      break
  elif g[x][y] == "R":
    if y != W-1:
      y += 1
    else:
      break

print(x+1,y+1)