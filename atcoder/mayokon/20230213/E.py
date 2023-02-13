INF = 10**18

N = int(input())
jumpers = []
for _ in range(N):
  x, y, P = (int(x) for x in input().split())
  jumpers.append((x, y, P))

def jumpable(S):
  graph = []
  for i in range(N):
    row = []
    x1, y1, P = jumpers[i]
    for j in range(N):
      x2, y2, _ = jumpers[j]
      if S * P >= abs(x1-x2) + abs(y1-y2):
        row.append(1)
      else:
        row.append(INF) 

    graph.append(row)

  for k in range(N):
    for i in range(N):
      for j in range(N):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

  for i in range(N):
    for j in range(N):
      if graph[i][j] == INF:
        break
    else:
      return True

  return False

ng, ok = 0, 10**18
while ok - ng > 1:
  m = (ok+ng) >> 1
  if jumpable(m):
    ok = m
  else:
    ng = m

print(ok)