from atcoder.lazysegtree import LazySegTree

W, N = (int(x) for x in input().split())
op = lambda a, b: max(a, b)
e = -10**18
id_ = 0 
mapping = lambda a, b: b if a == id_ else a
composition = lambda a, b: b if a == id_ else a
lst = LazySegTreeq(op=op, e=e, mapping=mapping, composition=composition, id_=id_, v=[0] * (W + 1))
for _ in range(N):
  L, R = (int(x) for x in input().split())
  L, R = L-1, R-1
  mx = lst.prod(L, R+1)
  lst.apply(L, R+1, mx+1)
  print(mx+1)
