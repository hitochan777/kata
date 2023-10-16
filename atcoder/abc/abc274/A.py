import math


A, B = (int(x) for x in input().split())
r = round(B / A, 3)
print("%.3f" % r)
