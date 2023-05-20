N, Q = (int(x) for x in input().split())
graph = {i: set() for i in range(1, N + 1)}
isolated_vertices = set(range(1, N + 1))
for _ in range(Q):
  query = list(int(x) for x in input().split())
  q_type = query[0]
  v = query[1]
  if q_type == 1:
    u = query[2]
    graph[v].add(u)
    graph[u].add(v)
    isolated_vertices.discard(v)
    isolated_vertices.discard(u)
  elif q_type == 2:
    isolated_vertices.add(v)
    for neighbor in graph[v]:
      graph[neighbor].remove(v)
      if len(graph[neighbor]) == 0:
        isolated_vertices.add(neighbor)

    graph[v].clear()

  print(len(isolated_vertices))