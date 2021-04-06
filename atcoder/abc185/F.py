class SegmentTree:
    def __init__(self, n, operator, identity):
        self.n = n
        self.array = [identity for i in range(2 ** (n + 1))]
        self.identity = identity
        self.operator = operator

    def update(self, x, val):
        x += self.n - 1
        self.array[x] = val
        while x > 0 :
            x = (x-1) >> 1
            self.array[x] = self.operator(self.array[x*2+1],self.array[x*2+2])

    def get(self, a, b, k = 0, l = 0, r = -1):
        if r < 0:
            r = self.n
        
        if r <= a or b <= l:
            return self.identity

        if a <= l and r <= b:
            return self.array[k]

        vl = self.get(a, b, 2 * k + 1, l , (l + r) >> 1)
        vr = self.get(a, b, 2 * k + 2, (l + r) >> 1 , r)
        return self.operator(vl, vr)

N, Q = (int(x) for x in input().split())
As = (int(x) for x in input().split())

st = SegmentTree(N, lambda a, b: a ^ b, 0)

for _ in range(Q):
    T, X, Y = (int(x) for x in input().split())
    X -= 1
    if T == 1:
        a = st.get(X, X+1)
        st.update(X, a ^ Y)
    else: # T = 2
        print(st.get(X, Y))
