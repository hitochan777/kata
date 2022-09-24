from os import rmdir


N = int(input())
P = [[0] * 1501 for _ in range(1501)]
for _ in range(N):
  X, Y = (int(x) for x in input().split())
  P[X][Y] += 1

for i in range(1, 1501):
  for j in range(1, 1501):
    P[i][j] += P[i][j-1]

for i in range(1, 1501):
  for j in range(1, 1501):
    P[i][j] += P[i-1][j]

Q = int(input())
for _ in range(Q):
  a, b, c, d = (int(x) for x in input().split())
  print(P[c][d] - P[c][b-1] - P[a-1][d] + P[a-1][b-1])