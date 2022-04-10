N, X, Y = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

def solve(A):
  n = len(A)
  m = n >> 1
  x1, x2 = solve(A[:m])
  y1, y2 = solve(A[m])