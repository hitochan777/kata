import heapq

N, Q = (int(x) for x in input().split())
not_called = list(range(1, N+1))
heapq.heapify(not_called)
called_once = []
visited = set()
for _ in range(Q):
  event = list(int(x) for x in input().split())
  cmd = event[0]
  if cmd == 1:
    x = heapq.heappop(not_called)
    heapq.heappush(called_once, x)
  elif cmd == 2:
    x = int(event[1])
    visited.add(x)
  else:
    while True:
      x = heapq.heappop(called_once)
      if x not in visited:
        print(x)
        heapq.heappush(called_once, x)
        break