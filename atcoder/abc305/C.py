H, W = (int(x) for x in input().split())
g = []
for _ in range(H):
  S = input()
  g.append(S)


for x in range(H-1):
  for y in range(W-1):
    cnt = sum(1 for i in range(x, x+2) for j in range(y, y+2) if g[i][j] == "#")
    if cnt != 3:
       continue

    for i in range(x, x+2):
      for j in range(y, y+2):
        if g[i][j] == ".":
          print(i+1, j+1)
          exit()