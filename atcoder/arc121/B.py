from bisect import bisect_left


N = int(input())
cnt = {"R": [], "G": [], "B": []}
for _ in range(N * 2):
  a, c = input().split()
  cnt[c].append(int(a))

cnts = []
for v in cnt.values():
  if len(v) % 2 != 0:
    cnts.append(v)

if len(cnts) == 0:
  print(0)
  exit()

assert len(cnts) == 2, len(cnts)
cnts[1].sort()
ans = 10**18
for n in cnts[0]:
  idx = bisect_left(cnts[1], n)
  ans = min(ans, abs(n - cnts[1][idx]))
  if idx > 0:
    ans = min(ans, abs(n - cnts[1][idx-1]))

print(ans)