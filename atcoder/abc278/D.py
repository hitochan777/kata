from collections import defaultdict
N = int(input())
A = list(int(x) for x in input().split())
Q = int(input())
offsets = defaultdict(int)
for i, a in enumerate(A):
  offsets[i] = a

base = 0
for _ in range(Q):
  q, *rest = (int(x) for x in input().split())
  if q == 1:
    base = rest[0]
    offsets = defaultdict(int)
  elif q == 2:
    offsets[rest[0]-1] += rest[1]
  else:
    print(base + offsets[rest[0]-1])
  
