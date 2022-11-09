from collections import defaultdict
import heapq

Q = int(input())
cnt = defaultdict(int)
h = [] 
total = 0
offset = 0
for _ in range(Q):
  query = list(int(x) for x in input().split())
  command = query[0]
  if command == 1:
    X = int(query[1]) - offset
    if cnt[X] == 0:
      heapq.heappush(h, X)

    cnt[X] += 1
    total += 1
  elif command == 2:
    X = int(query[1])
    offset += X
  else:
    val = heapq.heappop(h)
    cnt[val] -= 1
    if cnt[val] > 0:
      heapq.heappush(h, val)

    total -= 1
    print(val+offset)