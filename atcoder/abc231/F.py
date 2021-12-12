from atcoder.segtree import SegTree

N = int(input())
A = list(int(x) for x in input().split())
B = list(int(x) for x in input().split())
AD = {v: i for i, v in enumerate(sorted(set(A)))}
BD = {v: i for i, v in enumerate(sorted(set(B)))}
A = [AD[v] for v in A]
B = [BD[v] for v in B]

st = SegTree(lambda a, b: a + b, 0, N)
C = sorted(zip(A, B))
print(C)
ans = 0
i = 0
while i < N:
    cnt = 1
    st.set(C[i][1], st.get(C[i][1]) + 1)
    while i+1 < N and C[i] == C[i+1]:
      i += 1
      cnt += 1

    ans += cnt * (cnt + st.prod(C[i][1]+1, N))
    i += 1


print(ans)
