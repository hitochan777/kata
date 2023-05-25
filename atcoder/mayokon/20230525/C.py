N, M = (int(x) for x in input().split())
conds = []
for _ in range(M):
  A, B = (int(x) for x in input().split())
  conds.append([A, B])

K = int(input())
plates = []
for _ in range(K):
  C, D = (int(x) for x in input().split())
  plates.append([C, D])

ans = 0
for i in range(1<<K):
  selected = set()
  for j in range(K):
    selected.add(plates[j][(i >> j) & 1])

  tmp = sum(1 for a, b in conds if a in selected and b in selected)
  ans = max(ans, tmp)

print(ans)
