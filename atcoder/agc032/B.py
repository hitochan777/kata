N = int(input())
edges = []
for i in range(1, N+1):
  for j in range(i+1, N+1):
    if i + j == N + (1 if N % 2 == 0 else 0):
      continue

    edges.append((i, j))

print(len(edges))
for edge in edges:
  print(*edge)