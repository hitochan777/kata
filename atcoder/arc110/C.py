N = int(input())
P = list(int(x) for x in input().split())

target = 1
p = 0
ops = []
while p < N - 1:
  idx = P.index(target)
  i = idx
  for i in range(idx, max(target - 1, p), -1):
    P[i], P[i-1] = P[i-1], P[i]
    ops.append(i)
    i -= 1

  if not all(P[i] == i+1 for i in range(p, idx)):
    print("-1")
    exit()

  p = idx
  target = idx+1

for op in ops:
  print(op)