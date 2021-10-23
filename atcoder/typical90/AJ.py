N, Q = (int(x) for x in input().split())
pos = []
max_xp = -10**10 
min_xp = 10**10 
max_yp = -10**10 
min_yp = 10**10 
for _ in range(N):
  x, y = (int(x) for x in input().split())
  xp = x + y
  yp = x - y
  pos.append((xp, yp))
  max_xp = max(max_xp, xp)
  min_xp = min(min_xp, xp)
  max_yp = max(max_yp, yp)
  min_yp = min(min_yp, yp)

for _ in range(Q):
  q = int(input())
  xp, yp = pos[q-1]
  print(max(abs(xp - min_xp), abs(xp - max_xp), abs(yp - min_yp), abs(yp - max_yp)))

# https://kagamiz.hatenablog.com/entry/2014/12/21/213931
# this article hsa extremely nice explanation on manhattan distance