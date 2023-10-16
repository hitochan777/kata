from collections import defaultdict
import bisect

N = int(input())
m = defaultdict(list)
A = list(int(x) for x in input().split())
for i, a in enumerate(A, start=1):
  m[a].append(i)

Q = int(input())
for _ in range(Q):
  L, R, X = list(int(x) for x in input().split())
  l = bisect.bisect_left(m[X], L)
  r = bisect.bisect_right(m[X], R)
  print(r-l)
