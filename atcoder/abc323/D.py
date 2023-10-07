import heapq
from collections import defaultdict
N = int(input())

q = []
count = defaultdict(int)
ans = 0
for _ in range(N):
  S, V = (int(x) for x in input().split())
  heapq.heappush(q, S)
  count[S] = V

while q:
  s = heapq.heappop(q)
  # print(s)
  val = count[s] // 2
  ans += count[s] % 2
  if val > 0:
    if s * 2 not in count:
      heapq.heappush(q, s * 2)
    count[s*2] += val


print(ans)