import math
X, Y = (int(x) for x in input().split())
print(math.ceil(max(Y - X, 0) / 10))
