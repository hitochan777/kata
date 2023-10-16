from math import gcd
N = int(input())
num = 1
for _ in range(N):
  T = int(input())
  num = num * T // gcd(num, T)

print(num)