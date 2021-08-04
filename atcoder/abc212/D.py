import heapq

h = []
Q = int(input())
addition = 0
for _ in range(Q):
  q = [int(x) for x in input().split()]
  op = q[0]
  if op == 1:
    heapq.heappush(h, q[1] - addition)
  elif op == 2:
    addition += q[1]
  else:
    val = heapq.heappop(h) + addition
    print(val)