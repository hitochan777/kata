import numpy as np

H, W = list(int(x) for x in input().split())

matrix = []
for _ in range(H):
  li = list(int(x) for x in input().split())
  matrix.append(li)

s1 = np.sum(matrix, axis=1)
s2 = np.sum(matrix, axis=0)

ans = [[str(s1[i] + s2[j] - matrix[i][j]) for i in range(H)] for j in range(W)]
for li in ans:
  print(" ".join(li))