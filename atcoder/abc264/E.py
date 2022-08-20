from atcoder.dsu import DSU

N, M, E = (int(x) for x in input().split())
cables = []
for _ in range(E):
  U, V = (int(x)-1 for x in input().split())
  cables.append((U,V))

Q = int(input())
Xs = []
deadX = set()
for _ in range(Q):
  X = int(input())-1
  Xs.append(X)
  deadX.add(X)

Xs.reverse()
dsu = DSU(N+M)
lighted = set(range(N, N+M))

cnt = 0
for i, (u, v) in enumerate(cables):
  if i in deadX:
    print("hoge", i)
    continue

  if dsu.same(*cables[X]):
    continue

  if (dsu.leader(cables[X][0]) in lighted) != (dsu.leader(cables[X][1]) in lighted):
    if dsu.leader(cables[X][0]) not in lighted:
      cnt += dsu.size(cables[X][0])
      lighted.add(dsu.leader(cables[X][0]))
    else:
      cnt += dsu.size(cables[X][1])
      lighted.add(dsu.leader(cables[X][1]))

  dsu.merge(*cables[X])

print(dsu.groups())

ans = [cnt]
for X in Xs:
  cnt = ans[-1]
  if dsu.same(*cables[X]):
    ans.append(cnt)
    continue

  if (dsu.leader(cables[X][0]) in lighted) != (dsu.leader(cables[X][1]) in lighted):
    if dsu.leader(cables[X][0]) not in lighted:
      cnt += dsu.size(cables[X][0])
      lighted.add(dsu.leader(cables[X][0]))
    else:
      cnt += dsu.size(cables[X][1])
      lighted.add(dsu.leader(cables[X][1]))

  ans.append(cnt)
  dsu.merge(*cables[X])

for cnt in ans[0:-1][::-1]:
  print(cnt)