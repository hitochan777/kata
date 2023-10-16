import heapq

N, M = (int(x) for x in input().split())
P = list(int(x) for x in input().split())
L = list(int(x) for x in input().split())
D = list(int(x) for x in input().split())

ld = sorted(zip(L, D))
P.sort()
j = 0
q = []
discount = 0
for p in P:
  while j < M and ld[j][0] <= p:
    heapq.heappush(q, -ld[j][1])
    j += 1

  if q:
    discount += -heapq.heappop(q)

print(sum(P) - discount)

    
