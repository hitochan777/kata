from atcoder.fenwicktree import FenwickTree

def compress(nums):
  return {n: i for i, n in enumerate(nums)}

queries = []
Q = int(input())
for _ in range(Q):
  q = list(int(x) for x in input().split())
  queries.append(q)

nums = sorted(list(set([q[1] for q in queries])))
d = compress(nums)
N = len(d)
ft = FenwickTree(N)
for q in queries:
  c = q[0]
  x = d[q[1]]
  if c == 1:
    ft.add(x, 1)
  elif c == 2:
    k = q[2]
    ok, ng = -1, N
    while abs(ok - ng) > 1:
      m = (ok + ng) >> 1
      total = ft.sum(m, x+1) if 0 <= m <= x + 1 <= N else 0
      if total >= k:
        ok = m
      else:
        ng = m

    if ok >= 0:
      print(nums[ok])
    else:
      print(-1)

  else:
    k = q[2]
    ng, ok = -1, N
    while abs(ok - ng) > 1:
      m = (ok + ng) >> 1
      total = ft.sum(x, m+1) if 0 <= x <= m + 1 <= N else 0
      if total >= k:
        ok = m
      else:
        ng = m

    if ok < N:
      print(nums[ok])
    else:
      print(-1)