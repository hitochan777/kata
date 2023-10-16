N = int(input())
vals = set()
for a in range(2, 10 ** 5):
    cur = a * a
    while cur <= N:
        vals.add(cur)
        cur *= a

print(N - len(vals))