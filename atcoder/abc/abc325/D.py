import heapq
N = int(input())
products = []
for i in range(N):
  T, D = (int(x) for x in input().split())
  products.append((T, T+D))

products.sort()
ans = 0
t = 0
cur = 0
pq = []
while True:
  if len(pq) == 0:
    if cur >= N:
      break

    t = products[cur][0]

  while cur < N and products[cur][0] == t:
    heapq.heappush(pq, products[cur][1])
    cur += 1

  while pq:
    val = heapq.heappop(pq)
    if val >= t:
      heapq.heappush(pq, val)
      break

  if pq:
    heapq.heappop(pq)
    ans += 1
    t += 1

print(ans)

  
  
