import math

ls = sorted(list(int(x) for x in input().split()))
R = sum(ls)
r = max(0, ls[2] - (ls[0] + ls[1]))

print(math.pi * (R ** 2 - r ** 2))
