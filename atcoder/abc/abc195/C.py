N = int(input())

cur = N
digits = len(str(N))
total = 0
for d in range(digits, 1, -1):
    n = cur - 10**(d - 1) + 1
    total += n * ((d - 1) // 3)
    cur = 10**(d - 1) - 1

print(total)
