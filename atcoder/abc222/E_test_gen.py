N = 1000
M = 100
K = 10000
A = ["1", "100"] * 50
edges = [(i + 1, i + 2) for i in range(N-1)]
print(N, M, K)
print(" ".join(A))
for edge in edges:
  print(edge[0], edge[1])