from collections import defaultdict
import heapq

INF = 10**10

H, W = (int(x) for x in input().split())
Ch, Cw = (int(x)-1 for x in input().split())
Dh, Dw = (int(x)-1 for x in input().split())
g = []
for _ in range(H):
  g.append(input())

cost = defaultdict(lambda: (INF, INF))
hq = [((0, 0), (Ch, Cw))]

heapq.heapify(hq)
while hq:
  c, v = heapq.heappop(hq)
  if c > cost[v]:
    continue

  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    x, y = v[0] + dx, v[1] + dy
    if not (0 <= x <= H-1 and 0 <= y <= W-1):
      continue
    if g[x][y] == "#":
      continue

    c1, c2 = c
    tmp = (c1, c2+1)
    if tmp < cost[(x,y)]:
      cost[(x,y)] = tmp
      heapq.heappush(hq, (tmp, (x,y)))

  for dx in range(-2, 3):
    for dy in range(-2, 3):
      x, y = v[0] + dx, v[1] + dy
      if not (0 <= x <= H-1 and 0 <= y <= W-1):
        continue
      if g[x][y] == "#":
        continue

      c1, c2 = c
      tmp = (c1+1, c2+1)
      if tmp < cost[(x,y)]:
        cost[(x,y)] = tmp
        heapq.heappush(hq, (tmp, (x,y)))

c1, c2 = cost[(Dh, Dw)]
if c2 == INF:
  print(-1)
else:
  print(c1)
