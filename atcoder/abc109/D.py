H, W = (int(x) for x in input().split())
lines = []
ops = []
for i in range(H):
  A = list(int(x) for x in input().split())
  for j in range(0,W-1):
    if A[j] % 2 != 0:
      A[j+1] += 1
      ops.append((i+1, j+1, i+1, j+2))

  lines.append(A)

for i in range(0, H-1):
  if lines[i][-1] % 2 != 0:
    lines[i+1][-1] += 1
    ops.append((i+1, W, i+2, W))

print(len(ops))
for op in ops:
  print(*op)