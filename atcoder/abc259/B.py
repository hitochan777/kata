import math

a, b, d = (int(x) for x in input().split())

rad = math.radians(d)
x = math.cos(rad) * a - math.sin(rad) * b
y = math.sin(rad) * a + math.cos(rad) * b
print(x,y)