from collections import defaultdict, deque
N, M = (int(x) for x in input().split())
P = list(int(x) for x in input().split())
tree = defaultdict(set)
for i, p in enumerate(P, start=2):
  tree[p].add(i)

cnt = defaultdict(int)
for _ in range(M):
  x, y = (int(x) for x in input().split())
  cnt[x] = max(cnt[x], y+1)

q = deque()
q.appendleft(1)
ans = 0
while q:
  node = q.pop()
  validity = cnt[node]
  if validity > 0:
    ans += 1

  for child in tree[node]:
    cnt[child] = max(cnt[child], validity-1)
    q.appendleft(child)

print(ans)