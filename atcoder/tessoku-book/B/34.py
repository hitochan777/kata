from functools import reduce


N, X, Y = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

grundy = [0] * (X + Y)
for i in range(X+Y):
  transit = [False] * 3
  if i >= X:
    transit[grundy[i-X]] = True
  if i >= Y:
    transit[grundy[i-Y]] = True

  for j in range(3):
    if not transit[j]:
      grundy[i] = j
      break

lose = reduce(lambda a, b: a^grundy[b%(X+Y)], A, 0) == 0
if lose:
  print("Second")
else:
  print("First")
