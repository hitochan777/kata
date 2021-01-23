n, x = list(map(int, input().split()))
x *= 100

for i in range(n):
    v, p = list(map(int, input().split()))
    x -= v * p
    if x < 0:
        print(i+1)
        break
else:
    print(-1)