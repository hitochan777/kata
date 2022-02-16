H, W, K = (int(x) for x in input().split())
g = []
for _ in range(H):
  g.append([x for x in input()])

cnt = 1
for i in range(H):
  for j in range(W):
    if g[i][j] == "#":
      g[i][j] = cnt
      cnt += 1

for i in range(H):
  for j in range(1,W):
    if g[i][j] == ".":
      g[i][j] = g[i][j-1]

for i in range(H):
  for j in range(W-2, -1, -1):
    if g[i][j] == ".":
      g[i][j] = g[i][j+1]

for i in range(1,H):
  for j in range(W):
    if g[i][j] == ".":
      g[i][j] = g[i-1][j]

for i in range(H-2, -1, -1):
  for j in range(W):
    if g[i][j] == ".":
      g[i][j] = g[i+1][j]

for i in range(H):
  print(*g[i])