from collections import defaultdict
N, Q = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

cnt = defaultdict(int)
indices = defaultdict(lambda: defaultdict(int))
for i, a in enumerate(A):
  indices[a][cnt[a]+1] = i+1
  cnt[a] += 1

for _ in range(Q):
  x, k = (int(x) for x in input().split())
  if indices[x][k] == 0:
    print(-1)
  else:
    print(indices[x][k])