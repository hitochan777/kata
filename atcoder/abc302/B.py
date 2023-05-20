H, W = (int(x) for x in input().split())
g = []
for _ in range(H):
  S = input()
  g.append(S)

for i in range(H):
  for j in range(W):
    for dx in [-1, 0, 1]:
      for dy in [-1, 0, 1]:
        if dx == 0 and dy == 0:
          continue

        s = ""
        for k in range(5):
          x = i+(dx*k)
          y = j+(dy*k)
          if not (0 <= x < H and 0 <= y < W):
            break

          s += g[x][y]

        if s == "snuke":
          for k in range(5):
            x = i+(dx*k)
            y = j+(dy*k)       
            print(x+1, y+1)
          
          exit()