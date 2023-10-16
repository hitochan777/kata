from bisect import bisect_left
N, Q = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
A.sort()
for _ in range(Q):
  x = int(input())
  idx = bisect_left(A, x)
  print(N - idx)