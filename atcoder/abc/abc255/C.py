X, A, D, N = (int(x) for x in input().split())

if D >= 0:
  if X <= A:
    print(A-X)
    exit()

  if X >= (A + D * (N-1)):
    print(X - (A + D*(N-1)))
    exit()

  low, high = 0, N-1
  while abs(low - high) > 1:
    m = (high + low) >> 1
    if A + D * m >= X:
      high = m
    else:
      low = m

  ans = abs(X - (A + D * high))
  if 0 < high:
    ans = min(ans, abs(A + D * (high-1) - X))

  print(ans)

else:
  if X >= A:
    print(X-A)
    exit()

  if X <= (A + D * (N-1)):
    print((A + D*(N-1))-X)
    exit()

  low, high = 0, N-1
  while abs(low - high) > 1:
    m = (high + low) >> 1
    if A + D * m <= X:
      high = m
    else:
      low = m

  ans = abs(X - (A + D * high))
  if 0 < high:
    ans = min(ans, abs(A + D * (high-1) - X))

  print(ans)