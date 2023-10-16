N = int(input())
points = []
for _ in range(N):
  X, Y = (int(x) for x in input().split())
  points.append((X, Y))

cnt = 0
for i1 in range(N):
  for i2 in range(i1+1, N):
    for i3 in range(i2+1, N):
      S2 = abs((points[i1][0] - points[i3][0]) * (points[i2][1] - points[i3][1]) - (points[i2][0] - points[i3][0]) * (points[i1][1] - points[i3][1]))
      S = S2 / 2
      if S > 0:
        cnt += 1
      
print(cnt)