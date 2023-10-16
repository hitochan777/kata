H, W = (int(x) for x in input().split())
g = []
for _ in range(H):
  g.append(input())

dirs = [(0,0),(1,0),(0,1),(1,1)]
ans = 0
for i in range(H-1):
  for j in range(W-1):
    cnt = sum(1 for dx, dy in dirs if g[i+dx][j+dy] == "#")
    if cnt == 1 or cnt == 3:
      ans += 1

print(ans)
    