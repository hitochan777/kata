from collections import namedtuple
import math
from typing import List, Tuple

N, K = (int(x) for x in input().split())
Point = namedtuple("Point", ["x", "y"])


def same_line(p1: Point, p2: Point, p3: Point) -> bool:
  dx1 = p1.x - p2.x
  dx2 = p1.x - p3.x
  dy1 = p1.y - p2.y
  dy2 = p1.y - p3.y
  return dx2 * dy1 == dx1 * dy2


points: List[Point] = []
for _ in range(N):
  X, Y = (int(x) for x in input().split())
  points.append(Point(X, Y))

if K <= 1:
  print("Infinity")
  exit()

visited = set()
ans = 0
for i in range(N):
  for j in range(i+1,N):
    if (i, j) in visited:
      continue

    p1 = points[i]
    p2 = points[j]
    ps = [i, j]
    n = 2
    for k in range(j+1, N):
      if same_line(p1, p2, points[k]):
        n += 1
        ps.append(k)

    for l in range(n):
      for m in range(l+1, n):
        visited.add((ps[l],ps[m]))

    if n >= K:
      ans += 1

print(ans)