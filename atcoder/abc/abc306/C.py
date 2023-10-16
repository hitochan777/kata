from collections import defaultdict
d = defaultdict(list)
N = int(input())
A = list(int(x) for x in input().split())
for i, a in enumerate(A,start=1):
  d[a].append(i)

li = [0]*N
for i in range(1,N+1):
  d[i].sort()
  li[i-1] = (d[i][1], i)

li.sort()
ans = []
for _, i in li:
  ans.append(i)

print(*ans)