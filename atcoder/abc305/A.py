import math
N = int(input())
a = N // 5 * 5
b = math.ceil(N / 5) * 5

d1 = abs(a - N)
d2 = abs(b - N)
if d1 < d2:
    print(a)
else:
    print(b)
