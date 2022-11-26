import math
from decimal import Decimal

A, B = (int(x) for x in input().split())

def fn(k):
  t = Decimal(1+k)
  return A/math.sqrt(t) + B*k

# for i in range(100):
#   print(fn(i))
k = ((2*B/A)**(-2/3))-1
if k < 0:
  k = 0

ans = min(fn(math.ceil(k)), fn(math.floor(k)))
print("{:.8f}".format(ans))