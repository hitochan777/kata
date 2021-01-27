import math
a, b, h, m = list(map(int, input().split()))

alpha = (60 * h + m) / 720
beta = m / 60
cos = math.cos(2 * math.pi * (alpha - beta))

print(math.sqrt(a**2 + b**2 - 2 * a * b * cos))
