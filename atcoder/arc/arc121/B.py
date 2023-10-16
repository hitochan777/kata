from bisect import bisect_left

def find_min(a, b):
  ans = 10**18
  for n in a:
    idx = bisect_left(b, n)
    if idx < len(b):
      ans = min(ans, abs(n - b[idx]))

    if idx > 0:
      ans = min(ans, abs(n - b[idx-1]))
  
  return ans

N = int(input())
cnt = {"R": [], "G": [], "B": []}
for _ in range(N * 2):
  a, c = input().split()
  cnt[c].append(int(a))

odds, evens = [], []
for v in cnt.values():
  if len(v) % 2 == 0:
    evens.append(v)
  else:
    odds.append(v)

if len(odds) == 0:
  print(0)
  exit()

odds[1].sort()
evens[0].sort()
ans = find_min(odds[0], odds[1])
ans = min(ans, find_min(odds[0], evens[0]) + find_min(odds[1], evens[0]))
print(ans)