from bisect import bisect_left
N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

for i in range(1, N+1):
  idx = bisect_left(A, i)
  print(A[idx]-i)