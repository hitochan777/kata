H, W, K = (int(x) for x in input().split())
rows = []
blacks = 0
for _ in range(H):
  row = input()
  rows.append(row)
  blacks += row.count("#")

ans = 0
for i in range(1<<H):
  for j in range(1<<W):
    cnt = blacks
    for i2 in range(H):
      for j2 in range(W):
        if (i >> i2) & 1 == 0 and (j >> j2) & 1 == 0:
          continue
        
        if rows[i2][j2] == "#":
          cnt -= 1

    if cnt == K:
      ans += 1

print(ans)

