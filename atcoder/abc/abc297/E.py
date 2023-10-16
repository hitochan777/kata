import heapq
N, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
q = []
used = set()
for i, a in enumerate(A):
  if a not in used:
    q.append(a)
    used.add(a)

heapq.heapify(q)

li = []

while len(li) < K:
  val = heapq.heappop(q)
  li.append(val)
  for i, a in enumerate(A):
    if val+a not in used:
      used.add(val+a)
      heapq.heappush(q, val+a)

print(li[K-1])