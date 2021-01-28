N, M, X = list(map(int, input().split()))
rows = []
for _ in range(N):
    c, *al = list(map(int, input().split()))
    rows.append((c, al))
min_cost = 10**7
for i in range(1<<N):
    cost = 0
    points = [0] * M
    for j in range(N):
        if (i >> j) & 1 != 0:
            cost += rows[j][0]
            for k in range(M):
                points[k] += rows[j][1][k]
    if all(points[k] >= X for k in range(M)):
        min_cost = min(min_cost, cost)

print(min_cost if min_cost < 10**7 else -1)
