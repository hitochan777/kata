H, W = (int(x) for x in input().split())
matrix = []
for _ in range(H):
  matrix.append(input().split())

for i in range(W):
  line = []
  for j in range(H):
    line.append(str(matrix[j][i]))

  print(" ".join(line))
