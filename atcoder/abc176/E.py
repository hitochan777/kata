from collections import defaultdict
H, W, M = (int(x) for x in input().split())

pos = set()
hcnt = defaultdict(int)
wcnt = defaultdict(int)
for _ in range(M):
  h, w = (int(x) for x in input().split())
  hcnt[h] += 1
  wcnt[w] += 1
  pos.add((h,w))

hlist = sorted([(v, k) for k, v in hcnt.items()], reverse=True)
wlist = sorted([(v, k) for k, v in wcnt.items()], reverse=True)
hmax = hlist[0][0]
wmax = wlist[0][0]
ans = hmax + wmax
hlist = [k for v, k in hlist if v == hmax]
wlist = [k for v, k in wlist if v == wmax]
if all((h, w) in pos for h in hlist for w  in wlist):
  ans -= 1

print(ans)
