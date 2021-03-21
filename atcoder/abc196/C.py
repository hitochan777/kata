N = int(input())
l = len(str(N))

total = 0
for i in range(1, (l-1) // 2):
    total += (10 * i) - 1
