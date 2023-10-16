import math
A, B = (int(x) for x in input().split())
print(A // B + (1 if A % B > 0 else 0))