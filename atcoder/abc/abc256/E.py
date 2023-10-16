from atcoder.scc import SCCGraph

N = int(input())
X = list(int(x)-1 for x in input().split())
C = list(int(x) for x in input().split())

g = SCCGraph(N)
for i, x in enumerate(X):
  g.add_edge(i, x)

li = g.scc()
ans = 0
for group in li:
  if len(group) <= 1:
    continue

  ans += min(C[i] for i in group)
    
print(ans)