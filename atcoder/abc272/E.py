from collections import defaultdict
from email.policy import default


N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

vals = defaultdict(set)
for i in range(N):
  for j in range(M):
    val = A[i] + (j+1) * (i+1)
    if val > N:
      break

    if val >= 0:
      vals[j].add(val)

for m in range(M):
  for i in range(N+1):
    if i not in vals[m]:
      print(i)
      break


  
