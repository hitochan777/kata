N = int(input())
points = []
for _ in range(N):
  x, y = (int(x) for x in input().split())
  points.append((x,y))

for i, (x1, y1) in enumerate(points):
  for j, (x2, y2) in enumerate(points):
    for k, (x3, y3) in enumerate(points):
      if i == j or i == k or j == k:
        continue

      if (y3-y1)*(x2-x1) == (y2-y1)*(x3-x1):
        print("Yes")
        exit()

print("No")