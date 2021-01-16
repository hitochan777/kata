from collections import defaultdict

def find_optimal_cost(costs, k):
    cost = 0
    m = len(costs)
    sums = [0]
    maxs = [-1000000000] * m
    for i in range(m * 2):
        sums.append(costs[i % m] + sums[-1])

    for i in range(m):
        for j in range(m):
            maxs[j] = max(sums[i+j+1] - sums[i], maxs[j])

    if sums[m] > 0:
        cost += sums[m] * (k // m)

    r = k % m
    mx = -10000000000
    for i in range(1, r + 1):
        mx = max(mx, maxs[i - 1])

    cost += mx
    return cost

n, k = list(map(int, input().split()))
ps = list(map(int, input().split()))
cs = list(map(int, input().split()))
visited = set()
cost_groups = []
for i in range(n):
    costs = []
    cur = i
    while True:
        if cur in visited:
            break
    
        costs.append(cs[cur])
        visited.add(cur)
        cur = ps[cur] - 1

    if len(costs) > 0:
        cost_groups.append(costs)

print(max(find_optimal_cost(costs, k) for costs in cost_groups))