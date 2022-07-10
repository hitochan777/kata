from atcoder.dsu import DSU

N = int(input())
sx, sy, tx, ty = (int(x) for x in input().split())
cs = []
for _ in range(N):
  x, y, r = (int(x) for x in input().split())
  cs.append((x,y,r))

dsu = DSU(N)
for i in range(N):
  for j in range(i+1,N):
    x1, y1, r1 = cs[i]
    x2, y2, r2 = cs[j]
    ds = (x1-x2)**2 + (y1-y2)**2
    d1 = abs(r1 - r2)
    d2 = r1 + r2
    if d1**2 == ds or d2**2 == ds:
      dsu.merge(i,j)

    if d1**2 < ds < d2**2:
      dsu.merge(i,j)

first = None 
for i in range(N):
  x, y, r = cs[i]
  if (x-sx)**2 + (y-sy)**2 == r**2:
    first = i
    break

second = None 
for i in range(N):
  x, y, r = cs[i]
  if (x-tx)**2 + (y-ty)**2 == r**2:
    second = i
    break

if dsu.same(first,second):
  print("Yes")
else:
  print("No")

