n = int(input())
al = list(map(int, input().split()))

max_total = 0
for l in range(n):
    min_val = 100000000000
    for r in range(l, n):
        min_val = min(min_val, al[r])
        total = min_val * (r - l + 1)
        max_total = max(max_total, total)

print(max_total)