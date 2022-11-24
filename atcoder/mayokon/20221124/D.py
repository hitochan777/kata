from heapq import heappop, heappush
from collections import deque

N = int(input())
h = []
q = deque()
for _ in range(N):
  query = list(x for x in input().split())
  cmd = int(query[0])
  if cmd == 1:
    x = int(query[1])
    q.append(x)
  elif cmd == 2:
    if len(h) > 0:
      print(heappop(h))
    else:
      print(q.popleft())
  else:
    while len(q) > 0:
      heappush(h, q.popleft())