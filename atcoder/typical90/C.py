from collections import defaultdict

graph = defaultdict(list)

N = int(input())
for _ in range(N-1):
  A, B = (int(x) for x in input().split())
  A, B = A-1, B-1
  graph[A].append(B)
  graph[B].append(A)

def get_max_dist(node, graph):
  visited = set()
  return _get_max_dist(node, graph, visited, 0)

def _get_max_dist(node, graph, visited, dist):
  if node in visited:
    return dist - 1, None

  visited.add(node)
  max_dist = dist
  max_node = node
  for nb in graph[node]:
    cur_dist, cur_node = _get_max_dist(nb, graph, visited, dist+1)
    if cur_dist > max_dist:
      max_dist = cur_dist
      max_node = cur_node

  return max_dist, max_node


dist, node = get_max_dist(0, graph)
dist, node = get_max_dist(node, graph)
print(dist+1)
