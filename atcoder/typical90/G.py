from bisect import bisect_left

N = int(input())
A = list(int(x) for x in input().split())
A.sort()
Q = int(input())
for _ in range(Q):
  B = int(input())
  idx = bisect_left(A, B)
  print(min(abs(A[idx-1] - B), abs(A[idx % N] - B)))
