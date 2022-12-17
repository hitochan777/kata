from math import ceil
X, Y, R = (int(float(x)*1000) for x in input().split())

ans = 0
for y in range(ceil((Y-R)/1000),int((Y+R)/1000)+1):
  y *= 1000
  K = (R**2-(y-Y)**2)**0.5
  diff = (int(K-X) - ceil(-K-X)) // 1000 + 1
  print(diff)
  ans += diff

print(ans)
