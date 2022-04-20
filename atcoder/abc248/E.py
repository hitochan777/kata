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

def get_hash(p1: Point, p2: Point) -> Tuple[int, int, int, int]:
  a, b = p1.y - p2.y, p1.x - p2.x
  if a != 0 and b != 0:
    g = math.gcd(a, b)
    a, b = a // g, b // g
  else:
    if a != 0:
      a = 1
    else:
      b = 1

  c, d = p1.x * p2.y - p2.x * p1.y, p1.x - p2.x
  if c != 0 and d != 0:
    g = math.gcd(c, d)
    c, d = c // g, d // g
  else:
    if c != 0:
      c = 1
    else:
      d = 1

  return (a, b, c, d)


points: List[Point] = []
for _ in range(N):
  X, Y = (int(x) for x in input().split())
  points.append(Point(X, Y))

if K <= 1:
  print("Infinity")
  exit()

s = set()
for i in range(N):
  for j in range(i+1,N):
    p1 = points[i]
    p2 = points[j]
    n = sum(1 for k in range(j+1, N) if same_line(p1, p2, points[k])) + 2
    if n >= K:
      h = get_hash(p1, p2)
      s.add(h)

print(len(s))