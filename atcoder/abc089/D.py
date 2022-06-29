def manhattan_dist(t1, t2):
  return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

H, W, D = (int(x) for x in input().split())
loc = {}
for i in range(H):
  A = list(int(x)-1 for x in input().split())
  for j, a in enumerate(A):
    loc[a] = (i,j)
    
acc = []
for i in range(D):
  li = [0]
  for j in range(i,H*W-D,D):
     li.append(manhattan_dist(loc[j], loc[j+D]) + li[-1])
     
  acc.append(li)
    
Q = int(input())
for _ in range(Q):
  L, R = (int(x)-1 for x in input().split())
  i = L % D
  print(acc[i][R//D]-acc[i][L//D])
  