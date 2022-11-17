from atcoder.dsu import DSU
L, Q = (int(x) for x in input().split())
dsu = DSU(L)
ops = []
cut = set()
for _ in range(Q):
  c, x = (int(x) for x in input().split())
  x -= 1
  ops.append((c,x))
  if c == 1:
    cut.add(x)

for i in range(L-1):
  if i not in cut:
    dsu.merge(i, i+1)

ans = []
for c, x in ops[::-1]:
  if c == 1:
    dsu.merge(x, x+1)
  else:
    ans.append(dsu.size(x))

for a in ans[::-1]:
  print(a)
  
