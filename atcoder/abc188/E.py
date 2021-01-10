from collections import defaultdict

n, m = list((map(int, input().split())))
costs = list((map(int, input().split())))


graph = defaultdict(list)
for _ in range(m):
    x, y = list((map(int, input().split())))
    graph[x-1].append(y-1)

############# Using graph search ################
# max_costs = {}

# def get_max_cost(node):
#     if node in max_costs:
#         return max_costs[node]

#     if len(graph[node]) == 0:
#         max_cost = None
#     else:
#         max_cost = -10000000000000000
#         for nb in graph[node]:
#             mx = get_max_cost(nb)
#             if mx == None:
#                 mx = 0

#             max_cost = max(max_cost, mx, costs[nb])

#     max_costs[node] = max_cost 
#     return max_cost

# profits = []
# for node in range(n):
#     max_cost = get_max_cost(node)
#     if max_cost is None:
#         continue

#     profits.append(max_cost - costs[node])

# if len(profits) == 0:
#     print(0)
# else:
#     print(max(profits))

dp = [1000000000000000] * n

for i in range(n):
    for j in graph[i]:
        dp[j] = min(dp[j], dp[i], costs[i])
    
print(max(costs[i] - dp[i] for i in range(len(costs))))