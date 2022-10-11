from collections import defaultdict, deque


N, M = (int(x) for x in input().split())

squares = {}
i = 0
while i**2 <= M:
  squares[i**2] = i
  i += 1

g = defaultdict(set)
for i in range(N):
  for j in range(N):
    for y in range(N):
      s = M - (y-j)**2
      if s not in squares:
        continue

      r = squares[s]
      if 0 <= i - r <= N:
        g[(i,j)].add((i-r,y))

      if 0 <= i + r <= N:
        g[(i,j)].add((i+r,y))


dist = defaultdict(lambda: 10**18)
dist[(0,0)] = 0
q = deque()
q.appendleft((0,0,-1))
visited = set()
while len(q):
  i, j, d = q.pop()
  visited.add((i,j))
  dist[(i,j)] = d + 1
  for ni, nj in g[(i,j)]:
    if (ni, nj) in visited:
      continue

    q.appendleft((ni,nj,d+1))

for i in range(N):
  row = [dist[(i,j)] for j in range(N)]
  print(*row)
