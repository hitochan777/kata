
s = set()
N, M = (int(x) for x in input().split())
for _ in range(M):
  k, *x = (int(x) for x in input().split())
  for i in range(k):
    for j in range(i+1, k):
      s.add((x[i],x[j]))

if len(s) == N * (N-1) // 2:
  print("Yes")
else:
  print("No")
