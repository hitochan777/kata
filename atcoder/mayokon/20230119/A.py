from collections import Counter
N, M = (int(x) for x in input().split())
A = Counter(int(x) for x in input().split())
B = Counter(int(x) for x in input().split())

for k, v in B.items():
  if k not in A or A[k] < B[k]:
    print("No")
    exit()
else:
  print("Yes")