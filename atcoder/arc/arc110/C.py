N = int(input())
P = list(int(x) for x in input().split())

target = 1
ops = []
for i, v in enumerate(P):
  if v == target:
    for j in range(i, target-1, -1):
      P[j], P[j-1] = P[j-1], P[j]
      ops.append(j)

    target = i + 1

if not all(i == v for i, v in enumerate(P, start=1)):
  print("-1")
  exit()

if len(ops) != N-1:
  print(-1)
  exit()

for op in ops:
  print(op)