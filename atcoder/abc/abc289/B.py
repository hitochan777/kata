from atcoder.dsu import DSU

N, M = (int(x) for x in input().split())
A = list(int(x)-1 for x in input().split())
dsu = DSU(N)
for a in A:
  dsu.merge(a, a+1)

read = set()
cur = 0
ans = []
while cur < N:
  while cur in read:
    cur += 1

  if cur >= N:
    break

  for g in dsu.groups():
    if cur in g:
      for val in sorted(g, reverse=True):
        ans.append(val+1)
        read.add(val)

      break

print(*ans) 
