import math

N = int(input())
A = list(int(x) for x in input().split())
val = A[0]
for a in A[1:]:
  val = math.gcd(val, a)

print(val)