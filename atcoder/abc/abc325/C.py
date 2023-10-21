from collections import deque
H, W = (int(x) for x in input().split())
g = []
for _ in range(H):
  S = list(input())
  g.append(S)

visited = set()
ans = 0
q = deque()

for h in range(H):
  for w in range(W):
    if (h, w) in visited or g[h][w] == ".":
      continue

    q.appendleft((h, w))
    while q:
      x, y = q.pop()
      visited.add((x,y))
      for dx in range(-1, 2):
        for dy in range(-1, 2):
          nx, ny = x + dx, y + dy
          if 0 <= nx < H and 0 <= ny < W and (nx, ny) not in visited and g[nx][ny] == "#":
            visited.add((nx, ny))
            q.appendleft((nx, ny))

    ans += 1    

print(ans)
