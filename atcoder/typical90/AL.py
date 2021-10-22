import math

A, B = (int(x) for x in input().split())
g = math.gcd(A, B)
ans = A * B // g
if ans > 10**18:
  print("Large")
else:
  print(ans)