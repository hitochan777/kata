H, W = (int(x) for x in input().split())
lines = []
for _ in range(H):
  line = list(int(x) for x in input().split())
  lines.append(line)

ok = True
for i1 in range(H):
  for i2 in range(i1+1, H):
    for j1 in range(W):
      for j2 in range(j1+1, W):
        if lines[i1][j1] + lines[i2][j2] > lines[i2][j1] + lines[i1][j2]:
          ok = False
          break

if ok:
  print("Yes")
else:
  print("No")

