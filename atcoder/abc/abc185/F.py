class SegmentTree:
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length()
        self.default = default
        self.dat = [default]*(self.size*2-1) 
        self.f = f

    def update(self, i, x):
        i += self.size-1
        self.dat[i] = x
        while i > 0:
            i = (i-1) >> 1
            self.dat[i] = self.f(self.dat[i*2+1], self.dat[i*2+2])

    def query(self, l, r, k=0, L=0, R=None):
        if R is None:
            R = self.size
        if R <= l or r <= L:
            return self.default
        if l <= L and R <= r:
            return self.dat[k]
        else:
            lres = self.query(l, r, k*2+1, L, (L+R) >> 1)
            rres = self.query(l, r, k*2+2, (L+R) >> 1, R)
            return self.f(lres, rres)

N, Q = (int(x) for x in input().split())
As = (int(x) for x in input().split())

st = SegmentTree(N, lambda a, b: a ^ b)
for i, a in enumerate(As):
    st.update(i, a)

for _ in range(Q):
    T, X, Y = (int(x) for x in input().split())
    X -= 1
    if T == 1:
        a = st.query(X, X+1)
        st.update(X, a ^ Y)
    else: # T = 2
        print(st.query(X, Y))