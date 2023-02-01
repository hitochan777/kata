from math import gcd
N = int(input())
magics = set()
pos = []
for _ in range(N):
    x, y = (int(x) for x in input().split())
    pos.append((x,y))

for i in range(N):
  x1, y1 = pos[i]
  for j in range(i+1,N):
    x2, y2 = pos[j]
    dx = x1 - x2
    dy = y1 - y2
    g = gcd(dx, dy)
    dx //= g
    dy //= g
    magics.add((dx,dy))
    magics.add((-dx,-dy))

print(len(magics))

