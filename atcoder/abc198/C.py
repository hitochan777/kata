import math
 
R, X, Y = (int(x) for x in input().split())
 
d = int(math.sqrt(X * X + Y * Y) * 10**6)
# when math.dist is used, one test case fails...
# d = int(math.dist([0, 0], [X, Y]) * 10**6)
R *= 10**6
 
cnt = max(0, d - R) // R
rem = d - R * cnt
if rem == 0:
    pass
elif rem % R == 0:
    cnt += 1
else:
    cnt += 2 
 
print(cnt)