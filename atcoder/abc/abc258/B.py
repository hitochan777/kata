N = int(input())
g = []
for _ in range(N):
  A = list(int(x) for x in list(input()))
  g.append(A)
  
dxs = [-1, 0, 1]
dys = [-1, 0, 1]

dirs = [(dx, dy) for dx in dxs for dy in dys if dx != 0 or dy != 0]

ans = 0
for dx, dy in dirs:
  for i in range(N):
    for j in range(N):
      val = g[i][j]
      x, y = i, j 
      for k in range(N-1):
        x = (x + dx) % N
        y = (y + dy) % N
        val = val * 10 + g[x][y]
        
      ans = max(val, ans) 
      
print(ans)
        
        