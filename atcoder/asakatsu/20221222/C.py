from functools import lru_cache
N = int(input())

@lru_cache
def fn(n):
  if n == 0:
    return 1

  return fn(n//2) + fn(n//3)

print(fn(N))
