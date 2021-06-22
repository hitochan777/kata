import numpy as np
import sys

H, W = list(int(x) for x in input().split())

def readline():
  return sys.stdin.readline()

def writeline(s: str):
  sys.stdout.write(s + "\n")

matrix = []
for _ in range(H):
  li = list(int(x) for x in readline().split())
  matrix.append(li)

matrix = np.array(matrix)

s1 = np.sum(matrix, axis=1)
s1 = np.tile(s1, (W, 1))
s1 = s1.transpose()
s2 = np.sum(matrix, axis=0)
s2 = np.tile(s2, (H, 1))

rows = s1 + s2 - matrix
for row in rows:
  writeline(" ".join(map(str, row)))

# ans = [[str(s1[i] + s2[j] - matrix[i][j]) for j in range(W)] for i in range(H)]
# for li in ans:
#   writeline(" ".join(li))