from collections import defaultdict, deque
import sys

N, M = (int(x) for x in input().split())

squares = {}
i = 0
while i**2 <= M:
  squares[i**2] = i
  i += 1

g = defaultdict(set)
for j in range(N):
  for y in range(N):
    s = M - (y-j)**2
    if s not in squares:
      continue

    r = squares[s]
    for i in range(N):
      if 0 <= i - r < N:
        g[(i,j)].add((i-r,y))

      if 0 <= i + r < N:
        g[(i,j)].add((i+r,y))


dist = defaultdict(lambda: 10**18)
dist[(0,0)] = 0
q = deque()
q.appendleft((0,0,-1))
visited = set()
visited.add((0,0))
cnt = 0
while len(q):
  i, j, d = q.pop()
  dist[(i,j)] = d + 1
  for ni, nj in g[(i,j)]:
    if (ni, nj) in visited:
      continue

    visited.add((ni,nj))
    q.appendleft((ni,nj,d+1))

for i in range(N):
  row = [dist[(i,j)] if dist[(i,j)] != 10**18 else -1 for j in range(N)]
  print(*row)
