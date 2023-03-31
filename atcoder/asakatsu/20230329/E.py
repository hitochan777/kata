import math
N = int(input())
t, a = 1, 1
for _ in range(N):
    T, A = (int(x) for x in input().split())
    n = max(math.ceil(t/T), math.ceil(a/A))
    t = n * T
    a = n * A

print(t+a)


