from collections import defaultdict

N, M = (int(x) for x in input().split())

cnt = [1] * N
has_red = defaultdict(bool)
has_red[0] = True

for _ in range(M):
  x, y = (int(x) for x in input().split())
  x, y = x-1,y-1
  if has_red[x]:
    has_red[y] = True
    if cnt[x] == 1:
      has_red[x] = False

  cnt[x] -= 1
  cnt[y] += 1

print(sum(1 for ok in has_red.values() if ok))