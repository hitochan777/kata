from bisect import bisect_left

N, Q = (int(x) for x in input().split())
A = list(int(x) for x in input().split())
A.sort()
idx = 1
ranges = []
acc = []
for a in A:
  if idx <= a - 1:
    ranges.append((idx, a - 1))
  
  idx = a + 1
else:
  ranges.append((idx, None))

s = 0
for r in ranges:
  if r[1] == None:
    s += 10**18
  else:
    s += r[1] - r[0] + 1
  
  acc.append(s)

# print(ranges)

for _ in range(Q):
  K = int(input())
  range_index = bisect_left(acc, K)
  offset = acc[range_index-1] if range_index > 0 else 0
  ans = ranges[range_index][0] + K - offset - 1
  print(ans)