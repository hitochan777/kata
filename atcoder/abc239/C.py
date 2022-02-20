x1, y1, x2, y2 = (int(x) for x in input().split())
dirs = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
for dx, dy in dirs:
  dx1 = abs(x1 + dx - x2) 
  dy1 = abs(y1 + dy - y2) 
  if (dx1 == 2 and dy1 == 1) or (dx1 == 1 and dy1 == 2):
    print("Yes")
    exit()

print("No")