from functools import reduce

N, H, W = (int(x) for x in input().split())
mountains = []
for _ in range(N):
  A, B = (int(x) for x in input().split())
  mountains.append(A-1)
  mountains.append(B-1)

if reduce(lambda a, b: a^b, mountains, 0) == 0:
  print("Second")
else:
  print("First")