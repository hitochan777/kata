N = int(input())

ans = 0
x = 1
while x * x <= N * 2:
    if (N * 2) % x != 0:
        x += 1
        continue

    y = N * 2 // x
    if (x & 1) != (y & 1):
        ans += 1

    x += 1

print(ans * 2)    
    


