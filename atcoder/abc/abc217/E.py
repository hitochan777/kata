import heapq
from collections import deque

Q = int(input())
q = deque()
mq = []

for _ in range(Q):
  tokens = list(int(x) for x in input().split())
  if tokens[0] == 1:
    x = tokens[1]
    q.append(x)
  elif tokens[0] == 2:
    if len(mq) == 0:
      print(q.popleft())
    else:
      print(heapq.heappop(mq))
  else:
    while len(q) > 0:
      val = q.pop()
      heapq.heappush(mq, val)