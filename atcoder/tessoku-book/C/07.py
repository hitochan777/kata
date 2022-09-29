from bisect import bisect_right


N = int(input())
C = list(int(x) for x in input().split())
C.sort()
for i in range(1,N):
  C[i] += C[i-1]

Q = int(input())
for _ in range(Q):
  X = int(input())
  idx = bisect_right(C, X)
  print(idx)