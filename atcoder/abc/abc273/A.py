def f(n):
  if n == 0:
    return 1

  return n * f(n-1)

N = int(input())
print(f(N))