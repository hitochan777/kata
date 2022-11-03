N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

ng, ok = 0, 10**18
while ok - ng > 1:
  m = (ok + ng) >> 1
  t = sum(min(a, m) for a in A)
  if t >= K:
    ok = m
  else:
    ng = m

K -= sum(min(a, ok-1) for a in A)
for i in range(N):
  A[i] -= min(A[i], ok-1)

i = 0
while K > 0:
  if A[i] > 0:
    A[i] -= 1
    K -= 1

  i += 1

print(*A)