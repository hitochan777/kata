n, k = map(int, input().split())

M = 10**9 + 7

total = 0
for i in range(k, n + 2):
    mn = (i - 1) * i // 2
    mx = (n) * (n+1) // 2 - (n-i) * (n-i+1) // 2
    subtotal = mx - mn  + 1
    total = (total + subtotal) % M

print(total)

