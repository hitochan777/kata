from collections import defaultdict

N = int(input())

cache = defaultdict(int)

def f(n):
  if n == 0:
    return 1

  if n // 2 not in cache:
    cache[n//2] = f(n//2)

  if n // 3 not in cache:
    cache[n//3] = f(n//3)

  two = cache[n//2]
  three = cache[n//3]
  return two + three

print(f(N))