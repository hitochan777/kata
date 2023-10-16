from collections import deque 
H, W = (int(x) for x in input().split())
grid = []
for _ in range(H):
  grid.append(input())

max_d = 0
q = deque()
q.appendleft((0,0,1))
added = set()
added.add((0,0))
while len(q) > 0:
  i, j, d = q.pop()
  max_d = max(max_d, d)

  if (i + 1, j) not in added and i + 1 < H and grid[i+1][j] == ".":
    added.add((i+1, j))
    q.appendleft((i + 1, j, d+1))

  if (i, j + 1) not in added and j + 1 < W and grid[i][j+1] == ".":
    added.add((i, j+1))
    q.appendleft((i, j + 1, d+1))

print(max_d)

  
