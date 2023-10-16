from collections import deque, defaultdict

H, W = (int(x) for x in input().split())
lines = []
for _ in range(H):
  lines.append(list(input()))

q = deque()
visited = set()
q.appendleft((1,1,0)) 
visited.add((1,1))
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

dist = defaultdict(lambda: 10**18) 
while len(q) > 0:
  x, y, d = q.pop()
  if lines[x-1][y-1] == "#":
    continue

  dist[(x,y)] = min(dist[(x,y)],d)
  for dx, dy in dirs: 
    pos = (x + dx, y + dy)
    if not (1 <= pos[0] <= H and 1 <= pos[1] <= W):
      continue

    if pos in visited:
      continue

    q.appendleft((pos[0],pos[1],d+1))
    visited.add(pos)

if dist[(H,W)] < 10**18:
  cnt = sum(1 for line in lines for c in line if c == "#")
  print(H  * W - dist[(H,W)] - cnt - 1)
else:
  print(-1)
