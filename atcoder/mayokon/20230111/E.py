from functools import reduce
from math import gcd, ceil

def lcm(a,b):
  return a * b // gcd(a,b)

N, M = (int(x) for x in input().split())
A = list(int(x)//2 for x in input().split())

l = reduce(lambda a,b: lcm(a,b),A,1)
if any((l // a) % 2 == 0 for a in A):
  print(0)
  exit()

print(ceil(M // l / 2))