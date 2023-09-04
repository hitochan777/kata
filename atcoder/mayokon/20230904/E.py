from functools import lru_cache
N = int(input())


@lru_cache(100000)
def f(n):
  if n == 1:
    return sum(range(1, 7)) / 6
  
  return sum(max(i, f(n-1)) for i in range(1, 7)) / 6

print(f(N))