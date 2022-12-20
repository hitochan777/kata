N, X, Y = (int(x) for x in input().split())

def red(n, c):
  if n == 1:
    return 0

  return red(n-1, c) + blue(n, X * c)

def blue(n, c):
  if n == 1:
    return c

  return red(n-1, c) + blue(n-1, Y * c)

print(red(N, 1))
