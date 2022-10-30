from collections import defaultdict

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

def dist2(a, b):
  return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

def is_square(points):
  cnt = defaultdict(int)
  for i in range(len(points)):
    for j in range(i+1, len(points)):
      d = dist2(points[i], points[j])
      cnt[d] += 1

  v = set(cnt.values())
  return 4 in v and 2 in v

g = []
for _ in range(9):
  g.append(input())

points = []
for i in range(9):
  for j in range(9):
    if g[i][j] == "#":
      points.append((i, j))

N = len(points)
cnt = 0
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      for l in range(k+1, N):
        a, b, c, d = Point(*points[i]), Point(*points[j]), Point(*points[k]), Point(*points[l])
        if is_square([a,b,c,d]):
          cnt += 1

print(cnt)