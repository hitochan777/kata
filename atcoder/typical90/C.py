from collections import defauldict

graph = defauldict(list)

N = int(input())
for _ in range(N):
  A, B = (int(x) for x in input().split())
  A, B = A-1, B-1
  graph[A] = B
  graph[B] = A

def get_max_dist(node, graph, visited, dist):
  if node in visited:
    return dist - 1

  visited.add(node)
  max_dist = dist
  for nb in graph[node]:
    cur_dist = get_max_dist(nb, graph, visited, dist+1)
    max_dist = max(max_dist, cur_dist)

  return max_dist

get_max_dist(0)
