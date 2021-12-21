N, M = (int(x) for x in input().split())
lines = [[0]*(M+2)]
for _ in range(N):
  lines.append([0] + [int(x) for x in input()] + [0])

lines.append([0]*(M+2))

directions = [(1,0),(0,1),(-1,0),(0,-1)]

initial = [[0] * M for _ in range(N)]
for i in range(1,N+1):
  for j in range(1,M+1):
    min_val = min(lines[i+dx][j+dy] for (dx, dy) in directions)
    initial[i-1][j-1] = min_val

for line in initial:
  print("".join(str(n) for n in line))
