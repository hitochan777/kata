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

    # print(sums[m])
    if sums[m] > 0:
        cost = sums[m] * (k // m - 1 if k % m == 0 else k // m) + max(maxs[i] for i in range(k % m if k % m > 0 else m))
    else:
        cost = max(maxs[i - 1] for i in range(1, m + 1))

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

# print(len(cost_groups))
print(max(find_optimal_cost(costs, k) for costs in cost_groups))

# assert find_optimal_cost([-1, -2, -3], 2) == -1
# assert find_optimal_cost([-1], 2) == -1
# assert find_optimal_cost([1, 10, -5], 10) == 6 * 3 + 10