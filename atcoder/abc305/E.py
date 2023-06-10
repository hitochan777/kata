from collections import defaultdict
import heapq

def find_guarded_vertices(guards):
    visited = set()
    q = []
    for v, h in guards:
      heapq.heappush(q, (-h, v))

    while q:
      h, v = heapq.heappop(q) 
      h = -h
      visited.add(v)
      if h > 0:
        for nb in g[v]:
          if nb not in visited:
            heapq.heappush(q, (-(h-1), nb))
            visited.add(nb)

    return sorted(visited)


N, M, K = map(int, input().split())
guards = []
g = defaultdict(set)
for _ in range(M):
  a, b = map(int, input().split())
  g[a].add(b)
  g[b].add(a)

for _ in range(K):
  p, h = map(int, input().split())
  guards.append((p, h))

guarded_vertices = find_guarded_vertices(guards)
print(len(guarded_vertices))
print(*guarded_vertices)
