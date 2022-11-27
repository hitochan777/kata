from atcoder.dsu import DSU
N, Q = (int(x) for x in input().split())
dsu = DSU(N+Q)
box2ld = list(range(N+Q))
ld2box = list(range(N+Q))
num = N

for _ in range(Q):
  q = list(int(x) for x in input().split())
  cmd = q[0]
  if cmd == 1:
    x, y = q[1]-1, q[2]-1
    if box2ld[y] == -1:
      continue

    if box2ld[x] == -1:
      box2ld[x], box2ld[y] = box2ld[y], -1
      ld2box[box2ld[x]] = x
    else:
      dsu.merge(box2ld[x],box2ld[y])
      box2ld[x], box2ld[y] = dsu.leader(box2ld[y]), -1
      ld2box[box2ld[x]] = x
  elif cmd == 2:
    x = q[1]-1
    if box2ld[x] == -1:
      box2ld[x], box2ld[num] = num, -1
      ld2box[num] = x
    else:
      dsu.merge(box2ld[x],num)
      box2ld[x], box2ld[num] = dsu.leader(num), -1
      ld2box[box2ld[x]] = x

    num += 1
  else:
    x = q[1]-1
    print(ld2box[dsu.leader(x)]+1)