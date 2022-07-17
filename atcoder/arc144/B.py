import math

N, a, b = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

good, bad = min(A), max(A)
while bad - good > 1:
  m = (bad + good) >> 1
  x, y = 0, 0
  for el in A:
    if el >= m:
      y += (el-m) // b
    else:
      x += math.ceil((m-el) / a)

  if x <= y:
    good = m
  else:
    bad = m

print(good)