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
  tmp = math.atan2(y, x) * 180 / math.pi
  return max(tmp, 360 - tmp)

def get_degree_size(d1, d2):
  # print(d1, d2)
  return min(abs(d1 - d2), 360 - abs(d1 - d2))

max_val = 0
for i in range(N):
  normalized_points = list(map(lambda p: get_degree(points[i], p), (p for k, p in enumerate(points) if k != i)))
  normalized_points.sort()
  # print(normalized_points)
  for j in range(N):
    if i == j:
      continue

    d = get_degree(points[i], points[j])
    # print(d)
    # print(i, j, d, normalized_points)
    idx = bisect_left(normalized_points, (d + 180) % 360)
    d2 = normalized_points[max(idx - 1, 0)]
    d3 = normalized_points[idx % (N - 1)] 
    max_val = max(max_val, get_degree_size(d, d2), get_degree_size(d, d3))

print(max_val)