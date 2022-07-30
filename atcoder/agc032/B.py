from collections import defaultdict
import itertools

N = int(input())
nums = [x+1 for x in range(N)]
subsets = [subset for subset in itertools.combinations(nums, 2)]

for i in range(1<<len(subsets)):
  if i == 0:
    continue

  cnt = defaultdict(int)
  edges = []
  for j in range(len(subsets)):
    if (i>>j) & 1 == 1:
      a, b = subsets[j]
      cnt[a] += b
      cnt[b] += a
      edges.append((a,b))

  s = set(cnt[num] for num in nums)
  if len(s) == 1:
    print(len(edges))
    for edge in edges:
      print(*edge)
    exit()

    