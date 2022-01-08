N, K = (int(x) for x in input().split())
P = list(int(x) for x in input().split())
P = P[::-1]

deleted = set()
ans = []
ans.append(N-K+1)
cur = N-K+1
for i in range(N-K):
  if cur <= P[i]:
    cur -= 1
    while cur in deleted:
      cur -= 1
  
  ans.append(cur)
  deleted.add(P[i])

for val in ans[::-1]:
  print(val)
  
  