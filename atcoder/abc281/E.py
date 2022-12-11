from collections import defaultdict
from heapq import heappush, heappop
cnt = defaultdict(list)
N, M, K = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
q = []

for i in range(K):
  heappush(q, A[i])
  cnt[A[i]] += 1

for i in range(N-M+1):
  val = heappop(q)




