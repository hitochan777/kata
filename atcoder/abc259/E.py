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
      d[p] = [min(e, x, y), max(e, x, y)]
  
  plili.append(pli)

# print(d)
# print(plili)
ans = set()
for pli in plili:
  li = []
  for p, e in pli:
    if (len(d[p]) == 1 and d[p][0] == e) or d[p][1] == e:
      if len(d[p]) == 1 or d[p][0] != d[p][1]:
        li.append(p)

  ans.add(tuple(li))
  # print(ans)

print(len(ans))
