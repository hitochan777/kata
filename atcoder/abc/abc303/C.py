N, M, H, K = (int(x) for x in input().split())
S = input()
items = set()
for _ in range(M):
  x, y = (int(x) for x in input().split())
  items.add((x,y))

dirs = {
  "R": (1, 0),
  "L": (-1, 0),
  "U": (0, 1),
  "D": (0, -1),
}
x, y = 0, 0
for c in S:
  dx, dy = dirs[c]
  H -= 1
  x += dx
  y += dy
  if H < 0:
    print("No")
    exit()

  if (x, y) in items and H < K:
    items.remove((x,y))
    H = K

print("Yes")

