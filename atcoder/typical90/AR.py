N, Q = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
shift = 0
for _ in range(Q):
  t, x, y = (int(x) for x in input().split())
  x, y = x-1, y-1
  if t == 1:
    x = (x - shift + N) % N
    y = (y - shift + N) % N
    A[x], A[y] = A[y], A[x]
  elif t == 2:
    shift += 1
    shift %= N
  else:
    x = (x - shift + N) % N
    print(A[x])