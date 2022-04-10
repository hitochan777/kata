N = int(input())

cache = [None] * 17
cache[1] = [1]

def fn(n):
  if cache[n] is not None:
    return cache[n]

  if n == 1:
    return [1]

  a = fn(n-1)
  b = [n]
  c = fn(n-1)
  cache[n] = a + b + c
  return cache[n]

print(*fn(N))