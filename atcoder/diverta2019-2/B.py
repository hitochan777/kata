N = int(input())

coords = []
for _ in range(N):
  x, y = (int(x) for x in input().split())
  coords.append((x,y))

min_val = N

for i in range(N):
  for j in range(N):
    if i == j:
      continue

    x1, y1 = coords[i]
    x2, y2 = coords[j]
    p, q = x1 - x2, y1 - y2
    cnt = 0
    for i2 in range(N):
      for j2 in range(N):
        if i2 == j2:
          continue

        x3, y3 = coords[i2]
        x4, y4 = coords[j2]
        if x3 - x4 == p and y3 - y4 == q:
          cnt += 1

    min_val = min(min_val, N - cnt)

print(min_val)