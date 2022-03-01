from atcoder.fenwicktree import FenwickTree

def compress(nums):
  return {n: i for i, n in enumerate(nums)}

queries = []
Q = int(input())
for _ in range(Q):
  q = list(int(x) for x in input().split())
  queries.append(q)

nums = sorted(list(set([q[1] for q in queries])))
print(nums)
d = compress(q)
print(d)
N = len(d)
ft = FenwickTree(N)
for q in queries:
  c = q[0]
  x = d[q[1]]
  if c == 1:
    ft.add(x, 1)
  elif c == 2:
    k = q[2]
    l, h = 0, N
    while l <= h:
      m = (l + h) >> 1
      total = ft.sum(m, x+1)
      if total >= k:
        l = m + 1
      else:
        h = m - 1

    if 0 <= l < N:
      print(nums[l])
    else:
      print(-1)

  else:
    k = q[2]
    l, h = 0, N
    while l <= h:
      m = (l + h) >> 1
      total = ft.sum(x, m+1)
      if total >= k:
        h = m + 1
      else:
        l = m - 1

    if 0 <= l < N:
      print(nums[l])
    else:
      print(-1)
    





