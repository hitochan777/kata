from collections import defaultdict
from email.policy import default

H, W = (int(x) for x in input().split())
lines = [["#"] * (W + 2)]
for _ in range(H):
    lines.append(["#"] + list(input()) + ["#"])

lines.append(["#"] * (W + 2))

ans = [["."] * W for _ in range(H)]

dirs = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2)]
m = defaultdict(int)

for i in range(1, H+1):
  for j in range(1, W+1):
    if lines[i][j] == "#":
      m[(i, j)] = False

for i in range(1, H+1):
  for j in range(1, W+1):
    if any(lines[i+dx][j+dy] == "." for dx, dy in dirs):
      continue

    for dx, dy in dirs:
      if (i+dx, j+dy) in m:
        m[(i+dx, j+dy)] = True

    ans[i-1][j-1] = "#"
      
if all(changed for changed in m.values()):
  print("possible")
  for i in range(H):
    print("".join(ans[i]))
else:
  print("impossible")
    

