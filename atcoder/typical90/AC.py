from atcoder.lazysegtree import LazySegTree

W, N = (int(x) for x in input().split())
op = lambda a, b: max(a, b)
e = -10**18
id_ = 0 
mapping = lambda a, b: a + b 
composition = lambda a, b: a + b
lst = LazySegTree(op=op, e=e, mapping=mapping, composition=composition, id_=id_, v=[0] * (5 * 10**5 + 1))
for _ in range(N):
  L, R = (int(x) for x in input().split())
  lst.apply(L, R+1, 1)
  print(lst.prod(L, R+1))