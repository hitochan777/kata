from functools import reduce
from math import gcd

N = int(input())
A = list(int(x) for x in input().split())

g = reduce(lambda a,b : gcd(a,b), A, A[0])
ans = 0
for a in A:
  n = a // g
  while n > 1 and n % 2 == 0:
    n //= 2
    ans += 1

  while n > 1 and n % 3 == 0:
    n //= 3
    ans += 1

  if n > 1:
    print(-1)
    exit()

print(ans)