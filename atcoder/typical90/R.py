import math

T = int(input())
L, X, Y = (int(x) for x in input().split())
Q = int(input())
for _ in range(Q):
  E = int(input())
  theta = 2 * math.pi * E / T
  base = math.sqrt(X ** 2 + (Y + L / 2 * math.sin(theta)) ** 2)
  height = L / 2 * (1 - math.cos(theta))
  # print(base, height)
  print(math.atan(height / base) / math.pi * 180)