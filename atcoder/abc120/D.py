from atcoder.dsu import DSU

N, M = (int(x) for x in input().split())
dsu = DSU(N)
ans = [N * (N-1)//2]
edges = []
for _ in range(M):
  A, B = (int(x)-1 for x in input().split()) 
  edges.append((A,B))

for A, B in edges[::-1]:
  dsu.merge(A, B)
  n = N - dsu.size(A)
  ans.append(n*(n-1)//2)
  
for val in ans[::-1]:
  print(val)