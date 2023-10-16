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

cnt, prev = 0, None
for i, item in enumerate(x_sorted):
  if prev != item.x:
    cnt += 1

  ans[item.index][0] = cnt
  prev = item.x

cnt, prev = 0, None
for i, item in enumerate(y_sorted):
  if prev != item.y:
    cnt += 1

  ans[item.index][1] = cnt
  prev = item.y


for i in range(N):
  x, y = ans[i+1]
  print(x, y)