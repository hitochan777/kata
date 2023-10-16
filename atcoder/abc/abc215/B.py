import math

N = int(input())
# print(int(math.log2(N)))

k = 0
cur = 1
while cur <= N:
  k += 1
  cur *= 2

print(k-1)