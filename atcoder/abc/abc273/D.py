from bisect import bisect_left, bisect_right
from collections import defaultdict


H, W, rs, cs = (int(x) for x in input().split())
rs, cs = rs, cs
N = int(input())
posr = defaultdict(list)
posc =  defaultdict(list)
for _ in range(N):
  r, c = (int(x) for x in input().split())
  posr[r].append(c)
  posc[c].append(r)

for k in posr.keys():
  posr[k].sort()

for k in posc.keys():
  posc[k].sort()


Q = int(input())
for _ in range(Q):
  d, l = (x for x in input().split())
  l = int(l)
  if d == "L":
    idx = bisect_left(posr[rs], cs)
    if idx == 0:
      cs -= l
    else:
      cs = max(cs-l, posr[rs][idx-1]+1)
  elif d == "R":
    idx = bisect_left(posr[rs], cs)
    if idx == len(posr[rs]):
      cs += l
    else:
      cs = min(cs+l, posr[rs][idx]-1)
  elif d == "D":
    idx = bisect_left(posc[cs], rs)
    if idx == len(posc[cs]):
      rs += l
    else:
      rs = min(rs+l, posc[cs][idx]-1)
  elif d == "U":
    idx = bisect_left(posc[cs], rs)
    if idx == 0:
      rs = rs-l
    else:
      rs = max(rs - l, posc[cs][idx-1]+1)

  rs = min(max(rs, 1), H)
  cs = min(max(cs, 1), W)
  
  print(rs, cs)