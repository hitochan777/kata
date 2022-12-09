N = int(input())
vals = []
nonzero = None
for _ in range(N):
  x, y, h = (int(x) for x in input().split())
  vals.append((x,y,h))
  if h > 0:
    nonzero = (x,y,h)

for cx in range(0,101):
  for cy in range(0,101):
    H = nonzero[2] + abs(nonzero[0]-cx) + abs(nonzero[1]-cy)
    if H <= 0:
      continue

    ok = True
    for x, y, h in vals:
      h2 = max(H - abs(x-cx) - abs(y-cy), 0)
      if h2 != h:
        ok = False
        break

    if ok:
      print(cx,cy,H)
      exit()


