N, K = list(int(x) for x in input().split())
A = list((int(x), i) for i, x in enumerate(input().split()))

A.sort()
base = K // N
extra_end_index = K % N

cnts = {}
for i, t in enumerate(A):
  cnts[t[1]] = base + (1 if i < extra_end_index else 0)

for i in range(N):
  print(cnts[i])
  

