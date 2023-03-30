# 2 3
# 3 3
# 3 2
# 6 4

# t = T / A * a

import math
N = int(input())
t, a = 1, 1
for _ in range(N):
    T, A = (int(x) for x in input().split())
    if T >= t:
      if A >= a:
        t = T
        a = A
      else:
        a = math.ceil(a / A) * A
        t = T * a // A
    else: # T < t
      if A >= a:
        t = math.ceil(t / T) * T
        a = A * t // T
      else:
        a, t = math.ceil(a / A) * A, T * a // A

    print(t,a )

print(t+a)


