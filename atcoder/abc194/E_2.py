N, M = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

idx = [[0] for _ in range(N)]
for i, a in enumerate(A, start=1):
  idx[a].append(i)

for i in range(N):
  idx[i].append(N+1)

for i in range(N):
  for j in range(len(idx[i])-1):
    if idx[i][j+1] - idx[i][j] > M:
      print(i)
      exit()

print(N)