N, Q = (int(x) for x in input().split())
li = []
for _ in range(N):
  L, *a = list(int(x) for x in input().split())
  li.append(a)

for _ in range(Q):
  s, q = (int(x)-1 for x in input().split())
  print(li[s][q])
  
