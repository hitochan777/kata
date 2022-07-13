from collections import defaultdict


d = defaultdict(list)
N = int(input())
plili = []
for _ in range(N):
  m = int(input())
  pli = []
  for _ in range(m):
    p, e = (int(x) for x in input().split())
    pli.append((p, e))
    if len(d[p]) == 0:
      d[p].append(e)
    elif len(d[p]) == 1:
      x = d[p][0]
      d[p] = [min(e, x), max(e, x)]
    else:
      x = d[p][0]
      y = d[p][1]
      d[p] = sorted([e,x,y])[1:]
  
  plili.append(pli)

ans = set()
for pli in plili:
  li = []
  for p, e in pli:
    if len(d[p]) == 1:
      li.append(p)
    elif d[p][1] == e and d[p][0] != d[p][1]:
      li.append(p)

  ans.add(tuple(li))

print(len(ans))
