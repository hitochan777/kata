import math
X, Y, R = (round(float(x)*10000) for x in input().split())

ans = 0
start = (Y-R) // 10000
end = (Y+R) // 10000
for y in range(start, end+1):
  val = R**2-(y*10000-Y)**2
  if val >= 0:
    # K = math.isqrt(val)
    K = int(val**0.5)
    diff = (X+K)//10000-(X-K-1)//10000
    ans += diff

print(ans)