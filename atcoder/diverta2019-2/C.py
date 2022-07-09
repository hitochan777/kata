import heapq

S = int(input())
A = sorted(list(int(x) for x in input().split()))
pluses = [A[-1]]
minuses = [A[0]]

for a in A[1:-1]:
  if a < 0:
    minuses.append(a)
  else:
    pluses.append(a)

ans = 0
ops = []
while len(pluses) > 1:
  m = minuses.pop()
  p = pluses.pop()
  ops.append((m, p))
  minuses.append(m-p)

ans = pluses[0]
for m in minuses:
  ops.append((ans, m))
  ans -= m

print(ans)
for op in ops:
  print(*op)
  
  