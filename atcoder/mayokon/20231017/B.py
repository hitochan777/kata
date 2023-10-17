import heapq
N, Q = (int(x) for x in input().split())

not_called = list(range(1, N+1))
heapq.heapify(not_called)
called = []
visited = set()
for _ in range(Q):
  a = list(int(x) for x in input().split())
  cmd = a[0]
  if cmd == 1:
    person = heapq.heappop(not_called)
    heapq.heappush(called, person)
  elif cmd == 2:
    x = a[1]
    visited.add(x)
  else:
    while True:
      person = heapq.heappop(called)
      if person not in visited:
        heapq.heappush(called, person)
        print(person)
        break