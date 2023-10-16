from collections import defaultdict, deque

H, W = (int(x) for x in input().split())
g = defaultdict(list)
g = []
S = None
for i in range(H):
  row = input()
  idx = row.find("S")
  if idx >= 0:
    S = (i, idx)

  g.append(row)

q = deque()
q.append((S, 0, None))
visited = {}

while len(q) > 0:
  p, dist, source = q.popleft()
  visited[p] = (dist, source)
  x, y = p
  for i, (dx, dy) in enumerate([(-1, 0), (1, 0), (0, -1), (0, 1)]):
    if not (0 <= x + dx < H and 0 <= y + dy < W):
      continue

    nb = (x+dx, y+dy)
    if g[nb[0]][nb[1]] == "#":
      continue

    if nb in visited:
      if visited[nb][0] + dist + 1 >= 4 and source is not None and source != visited[nb][1]:
        print("Yes")
        exit()
      else:
        continue

    new_source = source if source is not None else i
    q.append((nb, dist+1, new_source))
    visited[nb] = (dist+1, new_source)

print("No")