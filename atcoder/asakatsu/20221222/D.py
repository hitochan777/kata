from atcoder.dsu import DSU
N = int(input())
P = []
for _ in range(N):
  x, y = (int(x) for x in input().split())
  P.append((x,y))

ans = N
for i in range(N):
  for j in range(N):
    if i == j:
      continue

    x1, y1 = P[i]
    x2, y2 = P[j]
    p, q = x1-x2, y1-y2
    val = N
    dsu = DSU(N)
    for k in range(N):
      for l in range(N):
        x3, y3 = P[k]
        x4, y4 = P[l]
        if x3-x4 == p and y3-y4 == q and not dsu.same(k, l):
          val -= 1
          dsu.merge(k,l)


    ans = min(ans, val)

print(ans)

        
