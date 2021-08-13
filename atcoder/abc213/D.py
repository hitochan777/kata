from collections import defaultdict
import heapq

graph = defaultdict(list)
visited = set()

def find_minimum_unvisited(node: int):
  while len(graph[node]) > 0 and heapq.nsmallest(1, graph[node])[0] in visited:
    heapq.heappop(graph[node])

  if len(graph[node]) > 0:
    return heapq.nsmallest(1, graph[node])[0]

  return None

def dfs(node):
  if node in visited:
    return

  visited.add(node)
  print(node+1, end=" ")
  minimum = find_minimum_unvisited(node)
  if minimum is None:
    return

  while minimum is not None:
    dfs(minimum)
    print(node+1, end=" ")
    minimum = find_minimum_unvisited(node)

N = int(input())
for _ in range(N-1):
  A, B = (int(x) for x in input().split())
  A, B = A-1, B-1
  heapq.heappush(graph[A], B)
  heapq.heappush(graph[B], A)

dfs(0)