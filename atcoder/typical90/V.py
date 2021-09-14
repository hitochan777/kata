import math

A, B, C = (int(x) for x in input().split())

r = math.gcd(math.gcd(A, B), C)

print(A //r - 1 + B // r - 1 + C // r - 1)