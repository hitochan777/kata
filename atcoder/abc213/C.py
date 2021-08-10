from collections import namedtuple, defaultdict

H, W, N = (int(x) for x in input().split())
ans = defaultdict(lambda: [None, None])

points = [] 
Point = namedtuple("Point", "x y index")
for i in range(N):
  point = Point(*list(int(x) for x in input().split()), i + 1)
  points.append(point)

x_sorted = sorted(points, key=lambda p: p.x)
y_sorted = sorted(points, key=lambda p: p.y)

cnt = 1
for i, item in enumerate(x_sorted):
  ans[item.index][0] = i + 1

for i, item in enumerate(y_sorted):
  ans[item.index][1] = i + 1

for i in range(N):
  x, y = ans[i+1]
  print(x, y)