from collections import deque

def bfs(graph, start, k):
    queue = deque([(start, 0)])
    visited = set([start])
    total_sum = 0

    while queue:
        node, distance = queue.popleft()
        if distance <= k:
            total_sum += node

        if distance < k:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
                    visited.add(neighbor)

    return total_sum

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

Q = int(input())
for _ in range(Q):
    x, k = map(int, input().split())
    result = bfs(graph, x, k)
    print(result)