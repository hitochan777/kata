from collections import defaultdict
N = int(input())
A = []
max_val = defaultdict(lambda: (0, 0))
for _ in range(N):
  m = int(input())
  a = []
  for _ in range(m):
    p, e = (int(x) for x in input().split())
    a.append((p, e))
    if max_val[p][0] == e:
      max_val[p] = (max_val[p][0], max_val[p][1] + 1)
    elif max_val[p][0] < e:
      max_val[p] = (e, 1)
    
  A.append(a)

ans = 1
for a in A:
  for p, e in a:
    if max_val[p][0] == p and max_val[p][1] == 1:
      ans += 1

print(ans)
