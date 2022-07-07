import heapq

N = int(input())
S = list((int(x), i) for i, x in enumerate(input().split()))
L = [(-x, i) for x, i in S]
id = N

heapq.heapify(S)
heapq.heapify(L)

used = set()
li = []
for i in range(N-2):
  while True:
    x, j = heapq.heappop(S)
    if j not in used:
      used.add(j)
      break

  while True:
    y, j = heapq.heappop(L)
    if j not in used:
      used.add(j)
      break       

  z = x + y
  li.append((x, -y))
  heapq.heappush(S, (z, id))
  heapq.heappush(L, (-z, id))
  id += 1
  
x, _ = heapq.heappop(S)
y, _ = heapq.heappop(S)
li.append((y, x))
print(y-x)
for x, y in li:
  print(x, y)