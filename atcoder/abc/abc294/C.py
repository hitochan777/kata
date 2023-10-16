from collections import defaultdict
N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
C = []
for i, a in enumerate(A):
  C.append((a, i))

for i, b in enumerate(B, start=N):
  C.append((b, i))

C.sort()

ords = defaultdict(int)
for i, (val, j) in enumerate(C):
  ords[val] = i + 1

ans = []
for a in A:
  ans.append(ords[a])

print(*ans)

ans = []
for b in B:
  ans.append(ords[b])

print(*ans)




