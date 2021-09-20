N = int(input())

def make_array(*args, default=int):
  if len(args) == 0:
    return default()

  return [make_array(*args[1:], default=default) for _ in range(args[0])]

L = 1002
paper = make_array(L,L)

for _ in range(N):
  lx, ly, rx, ry = (int(x) for x in input().split())
  paper[lx][ly] += 1
  paper[lx][ry] -= 1
  paper[rx][ly] -= 1
  paper[rx][ry] += 1

for i in range(L):
  for j in range(1,L):
    paper[i][j] += paper[i][j-1]

for j in range(L):
  for i in range(1, L):
    paper[i][j] += paper[i-1][j]

areas = [0] * N
for i in range(L):
  for j in range(L):
    if paper[i][j] >= 1:
      areas[paper[i][j]-1] += 1

for area in areas:
  print(area)