H, W = (int(x) for x in input().split())
min_val = 100
rows = []
for _ in range(H):
    As = list(int(x) for x in input().split())
    rows.append(As)
    min_val = min(min_val, *As)

total = 0
for row in rows:
    for cell in row:
        total += cell - min_val

print(total)