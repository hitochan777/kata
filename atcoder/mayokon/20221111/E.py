import math
N = int(input())

def fn(n):
  if n == 1:
    return 3.5

  val = fn(n-1)
  res = sum(range(math.ceil(val), 7)) / 6
  res += math.floor(val) / 6 * val
  return res

print(fn(N))