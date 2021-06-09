from collections import defaultdict

N, M = (int(x) for x in input().split())

graph = defaultdict(list)
for _ in range(M):
    A, B = (int(x) for x in input().split())
    graph[A-1].append(B-1)

def dfs(n, visited):
    if n in visited:
        return

    visited.add(n)
    for neighbor in graph[n]:
        dfs(neighbor, visited)

total = 0
for i in range(N):
    visited = set()
    dfs(i, visited)
    total += len(visited)

print(total)