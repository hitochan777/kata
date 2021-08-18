from bisect import bisect_left, bisect_right

N = int(input())
A = list(int(x) for x in input().split())
A.sort()
Q = int(input())
for _ in range(Q):
  B = int(input())
  val1 = bisect_left(A, B)
  val2 = bisect_right(A, B)
  print(min(abs(val1 - B), abs(val2 - B)))
