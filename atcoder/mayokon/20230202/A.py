N, Q = (int(x) for x in input().split())
A = []
for _ in range(N):
  L, *a = (int(x) for x in input().split())
  A.append(a)

for _ in range(Q):
  s, t = (int(x)-1 for x in input().split())
  print(A[s][t])