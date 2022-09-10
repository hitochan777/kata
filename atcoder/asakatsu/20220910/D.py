from atcoder.segtree import SegTree

N, Q = (int(x) for x in input().split())
A = list(int(x) for x in input().split())

st = SegTree(op=lambda x, y: x ^ y, e=0, v=N)
for i, a in enumerate(A):
  st.set(i, a) 

for _ in range(Q):
  T, X, Y = (int(x) for x in input().split())
  if T == 1:
    X -= 1
    st.set(X, st.get(X)^Y)
  else:
    X, Y = X-1, Y-1
    print(st.prod(X, Y+1))