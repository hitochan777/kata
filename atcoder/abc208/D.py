import sys

N, M = list(map(int, sys.stdin.buffer.readline().split()))
ABC = map(int, sys.stdin.buffer.read().split())

INF = 1 << 60

dist = [[INF] * N for _ in range(N)]
for a, b, c in zip(ABC, ABC, ABC):
    a, b = a - 1, b - 1
    dist[a][b] = c

for i in range(N):
  dist[i][i] = 0

total = 0
for k in range(N):
  for i in range(N):
    for j in range(N):
      dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
      total += dist[i][j] if dist[i][j] < INF else 0 

print(total)