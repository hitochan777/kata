from bisect import bisect_left
import math

N = int(input())

points = []
for _ in range(N):
  x, y = (int(x) for x in input().split())
  points.append((x, y))

def get_vec(c, p):
  return p[0] - c[0], p[1] - c[1]

def get_degree(c, p):
  x, y = get_vec(c, p) 
  return math.atan2(y, x) * 180 / math.pi

def get_degree_size(d1, d2):
  return min(abs(d1 - d2), 360 - abs(d1 - d2))

max_val = 0
for i in range(N):
  for j in range(N):
    if i == j:
      continue

    d = get_degree(points[i], points[j])
    normalized_points = list(map(lambda p: get_degree_size(d, get_degree(points[i], p)), (p for k, p in enumerate(points) if k not in [i, j])))
    normalized_points.sort()
    # print(i, j, d, normalized_points)
    idx = bisect_left(normalized_points, 180)
    max_val = max(max_val, normalized_points[max(idx - 1, 0)])

print(max_val)