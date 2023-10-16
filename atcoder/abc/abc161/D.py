import heapq

K = int(input())

q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
heapq.heapify(q)
li = []
i = K
for _ in range(K):
    val = heapq.heappop(q)
    li.append(val)
    res = val % 10
    base = val * 10 + val % 10
    if res > 0:
        heapq.heappush(q, base - 1)
    
    heapq.heappush(q, base)
    if res < 9:
        heapq.heappush(q, base + 1)

print(li[K-1])