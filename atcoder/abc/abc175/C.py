x, k, d = list(map(int, input().split()))
x = abs(x)
s = min(k, x // d)
k -= s
x -= d * s

if k % 2 == 0:
    print(x)
else:
    print(d - x)