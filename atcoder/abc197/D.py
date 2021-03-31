import math

N = int(input())
x0, y0 = (int(x) for x in input().split())
xh, yh = (int(x) for x in input().split())

cx, cy = (xh + x0) / 2, (yh + y0) / 2

theta = math.atan2(y0 - cy, x0 - cx) + (2 * math.pi) / N
r = math.sqrt((xh - x0)**2 + (yh - y0)**2) / 2
print(math.sin(theta))
x1, y1 = r * math.cos(theta), r * math.sin(theta)
print(x1, y1)