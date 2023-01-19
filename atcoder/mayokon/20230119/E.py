from atcoder.scc import SCCGraph

N = int(input())
X = list(int(x)-1 for x in input().split())
C = list(int(x) for x in input().split())

g = SCCGraph(N)
for i,x in enumerate(X):
  g.add_edge(i, x)

ans = 0
for sc in  g.scc():
  if len(sc) > 1:
    ans += min(C[i] for i in sc)

print(ans)
