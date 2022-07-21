import math
N = int(input())
A = list(int(x) for x in input().split())

ans = 0
for i in range(N, 0, -1):
  pnode_min = math.ceil(A[i]/2)
  pnode_max = min(2**(min(i-1, 32)) - A[i-1], A[i])
  print(2**(min(i-1, 32)) - A[i-1], A[i])
  if pnode_min <= pnode_max:
    pnode = pnode_max
  else:
    print(-1)
    exit()

  ans += pnode
  ans += A[i]
  print(pnode, A[i], i, A)

print(ans)

   

