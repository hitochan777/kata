H, W = list(int(x) for x in input().split())

matrix = []
for _ in range(H):
  li = list(int(x) for x in input().split())
  matrix.append(li)

s1 = []
for row in matrix:
  s1.append(sum(row))

s2 = []
for j in range(W):
  s = sum(matrix[i][j] for i in range(H))
  s2.append(s)

ans = [[str(s1[i] + s2[j] - matrix[i][j]) for j in range(W)] for i in range(H)]
for li in ans:
  print(" ".join(li))