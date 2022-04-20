from collections import deque
H, W = (int(x) for x in input().split())
g = []
g.append(["#"] * (W + 2))
for _ in range(H):
  line = input()
  g.append(["#"] + list(line) + ["#"])

g.append(["#"] * (W + 2))

q = deque()
for i in range(1,H+1):
  for j in range(1,W+1):
    if g[i][j] == "#":
      q.appendleft((i,j))

d = [(-1,0), (1,0), (0,1),(0,-1)]
cnt = 0
while len(q) > 0:
  cnt += 1
  newq = deque()
  while len(q) > 0:
    h, w = q.pop()
    for dx, dy in d:
      if g[h + dx][w + dy] == ".":
        newq.appendleft((h+dx, w+dy))
        g[h+dx][w+dy] = "#"

  q = newq

print(cnt-1)