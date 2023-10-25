N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

ng, ok = -1, 10**12
while ok - ng > 1:
  m = (ok + ng) >> 1
  total = 0
  for a in A:
    total += min(a, m)

  if total >= K:
    ok = m
  else:
    ng = m

# print(ok)

total = 0
for i, a in enumerate(A):
  diff = min(a, ok-1)
  total += diff
  A[i] -= diff

i = 0
while total < K:
  if A[i] > 0:
    A[i] -= 1
    total += 1

  i += 1

print(*A)