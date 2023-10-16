import math
# A, B = list(int(x) for x in input().split())
P = int(input())

cnt = 0
for i in range(10,0,-1):
  fc = math.factorial(i)
  diff = min(P // fc, 100)
  P -= diff * fc
  cnt += diff

print(cnt)