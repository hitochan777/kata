def ok(x1, y1, x2, y2, Ps, K):
  cnt = 0
  for x, y in Ps:
    if x1 <= x <= x2 and y2 <= y <= y1:
      cnt += 1

    if cnt >= K:
      return True

  return False

N, K = (int(x) for x in input().split())
Xs = set()
Ys = set()
Ps = []
for _ in range(N):
  x, y = (int(x) for x in input().split())
  Ps.append((x, y))
  Xs.add(x)
  Ys.add(y)

ans = 10**20
for x1 in Xs:
  for y1 in Ys:
    for x2 in Xs:
      if x1 == x2:
        continue

      for y2 in Ys:
        if y1 == y2:
          continue

        if not (x1 < x2 and y1 > y2):
          continue

        if ok(x1, y1, x2, y2, Ps, K):
          ans = min((x2 - x1) * (y1 - y2), ans)

print(ans)

