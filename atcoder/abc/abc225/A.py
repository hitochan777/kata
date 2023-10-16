from collections import Counter
from math import factorial
S = input()

cnt = Counter(S)
vals = cnt.values()
tmp = 1
for val in vals:
  tmp *= factorial(val)

print(int(6/tmp))