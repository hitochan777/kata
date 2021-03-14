import math
A, B, W = list(int(x) for x in input().split())

mx = 1000 * W // A
mn = math.ceil(1000 * W / B)

if mx >= mn:
    print(mn, mx)
else:
    print("UNSATISFIABLE")