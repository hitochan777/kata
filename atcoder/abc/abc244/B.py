N = int(input())
T = input()

x, y = 0, 0
dx, dy = 1, 0
for t in T:
    if t == "R":
      dx, dy = dy, -dx
    else:
      x += dx
      y += dy

print(x, y)