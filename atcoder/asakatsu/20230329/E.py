import math
def ceil(a, b):
  return int(a // b + bool(a % b))

N = int(input())
t, a = 1, 1
for _ in range(N):
    T, A = (int(x) for x in input().split())
    n = max(ceil(t, T), ceil(a, A))
    t = n * T
    a = n * A

print(t+a)
